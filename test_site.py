from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import re
root=Path(__file__).parent
pages=['index.html','services/index.html','cases/index.html','about/index.html','contact/index.html','service/index.html','approach/index.html']
errors=[]
links=0
for name in pages:
 p=root/name
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 if name in pages[:5]:
  assert len(s.select('h1'))==1,(name,'H1',len(s.select('h1')))
  assert s.find('main',id='main'),(name,'no main')
  assert s.select_one('meta[name=robots]')['content']=='noindex,nofollow',name
  assert 'ZUN CONSULTING' in s.get_text(' ',strip=True)
 for a in s.select('[href]'):
  href=a.get('href')
  if href.startswith(('http:','https:','mailto:','tel:','data:')):continue
  links+=1
  hpath,_,frag=href.partition('#')
  if not hpath:dest=p
  else: dest=(p.parent/hpath).resolve()
  if hpath.endswith('/'):dest=dest/'index.html'
  if not dest.exists():errors.append((name,href,'target does not exist'));continue
  if frag:
   ts=BeautifulSoup(dest.read_text(encoding='utf-8'),'html.parser')
   if not ts.find(id=frag):errors.append((name,href,'fragment does not exist'))
assert not errors,errors
print(f'HTML + link check: PASS {len(pages)} pages, {links} links')
css=(root/'assets/style.css').read_text(encoding='utf-8')
js=(root/'assets/main.js').read_text(encoding='utf-8')
assert css.count('{')==css.count('}'),'CSS unbalanced'
assert 'hero-art.svg' not in (root/'index.html').read_text()
print('Legacy visual removed: PASS')
html=(root/'index.html').read_text(encoding='utf-8')
html=html.replace('<link rel="stylesheet" href="assets/style.css">','<style>'+css+'</style>')
html=html.replace('<script defer src="assets/main.js"></script>','')
html=html.replace('</body>','<script>'+js+'</script></body>')
(root/'preview.html').write_text(html,encoding='utf-8')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for name, w, h in [('desktop',1440,900),('mobile',390,844),('small-mobile',375,812),('tablet',768,1024)]:
  page=b.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
  exceptions=[]
  page.on('pageerror',lambda e: exceptions.append(str(e)))
  page.set_content(html,wait_until='load')
  assert page.evaluate('document.documentElement.scrollWidth')<=w,(name,'horizontal overflow')
  assert not exceptions,(name,exceptions)
  assert page.locator('h1').count()==1
  assert page.locator('.topic-list li').count()==4
  assert page.locator('.service-row').count()==4
  if name in ['desktop','mobile']:
   page.screenshot(path=str(root/f'preview-{name}.png'),full_page=True)
   page.screenshot(path=str(root/f'preview-{name}-first.png'),full_page=False)
  if w<760:
   btn=page.locator('.menu-button')
   assert btn.get_attribute('aria-expanded')=='false'
   btn.click()
   assert btn.get_attribute('aria-expanded')=='true',(name,'mobile nav did not open')
   assert page.locator('.nav').evaluate("n=>getComputedStyle(n).display")=='flex'
   page.keyboard.press('Escape')
   assert btn.get_attribute('aria-expanded')=='false'
  print(f'{name}: PASS, viewport={w} scrollWidth={page.evaluate("document.documentElement.scrollWidth")}')
  page.close()
 b.close()
print('Tests all passed')
