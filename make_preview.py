"""Build one-click, single-file offline preview from current home page."""
from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parent
page=BeautifulSoup((root/'index.html').read_text(encoding='utf-8'),'html.parser')
css=(root/'assets/style.css').read_text(encoding='utf-8')
js=(root/'assets/main.js').read_text(encoding='utf-8')
style=page.new_tag('style'); style.string=css
page.find('link',rel='stylesheet').replace_with(style)
script=page.find('script',src=True)
script.decompose()
inline_js=page.new_tag('script');inline_js.string=js
page.body.append(inline_js)
outer=page.select_one('.hero-art svg')
art=BeautifulSoup((root/'assets/hero-art.svg').read_text(encoding='utf-8'),'xml').find('svg')
placeholder=page.new_tag('div',id='art-svg-placeholder')
outer.replace_with(placeholder)
page.select_one('.hero')['id']='top'
link_map={'index.html':'#top','service/index.html':'#services-title','cases/index.html':'#case-title','approach/index.html':'#about-title','contact/index.html':'#contact-home-title'}
for a in page.select('a[href]'):
    href=a['href']
    for path, anchor in link_map.items():
        if href.startswith(path):
            a['href']=anchor
            break
fav=page.find('link',rel='icon')
if fav: fav.decompose()
robot=page.find('meta',attrs={'name':'robots'})
if robot:robot['content']='noindex,nofollow'
page.head.append(page.new_tag('meta',attrs={'name':'description','content':'Zun Consultingのオフラインデザインプレビュー。'}))
rendered='<!doctype html>\n'+str(page).replace('<!DOCTYPE html>','')
rendered=rendered.replace('<div id="art-svg-placeholder"></div>',(root/'assets/hero-art.svg').read_text(encoding='utf-8'))
(root/'preview.html').write_text(rendered,encoding='utf-8')
print('Created preview.html')
