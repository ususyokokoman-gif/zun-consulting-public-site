from pathlib import Path
from html import escape
import re
ROOT = Path(__file__).resolve().parent
BRAND = 'Zun Consulting'
SITE = 'https://ususyokokoman-gif.github.io/zun-consulting-public-site/'
NAV = [('/services/', '支援内容'),('/cases/', '相談事例'),('/about/', '担当者について'),('/contact/', '相談受付について')]

def href(root, path):
    p = path.lstrip('/')
    return ('../' if root else '') + p

def head(title, desc, root):
    home = 'index.html' if not root else '../index.html'
    css = 'assets/style.css' if not root else '../assets/style.css'
    ico = 'assets/favicon.svg' if not root else '../assets/favicon.svg'
    js = 'assets/main.js' if not root else '../assets/main.js'
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><meta name="theme-color" content="#192827"><meta name="robots" content="noindex,nofollow"><title>{escape(title)} | {BRAND}</title><meta name="description" content="{escape(desc)}"><link rel="icon" type="image/svg+xml" href="{ico}"><link rel="stylesheet" href="{css}"><script defer src="{js}"></script></head><body><a class="skip-link" href="#main">本文へ移動</a>'''

def header(root, current=None):
    home = '../index.html' if root else 'index.html'
    navlinks=''.join(f'<a href="{href(root,path)}"{(" aria-current=" + chr(34) + "page" + chr(34)) if path==current else ""}{" class=" + chr(34) + "nav-contact" + chr(34) if path=="/contact/" else ""}>{label}</a>' for path,label in NAV)
    return f'''<header class="header"><div class="header-in shell"><a class="brand" href="{home}" aria-label="Zun Consulting トップページへ"><span class="brand-mark" aria-hidden="true">Z</span><span><span class="brand-word">ZUN CONSULTING</span><span class="brand-sub">経営支援・業務改善</span></span></a><button class="menu-button" type="button" aria-label="メニューを開閉" aria-expanded="false" aria-controls="primary-nav"><span aria-hidden="true"></span></button><nav id="primary-nav" class="nav" aria-label="グローバルナビゲーション">{navlinks}</nav></div></header>'''

def footer(root):
    home='../index.html' if root else 'index.html'
    links=''.join(f'<a href="{href(root,path)}">{label}</a>' for path,label in NAV)
    return f'''<footer class="footer"><div class="shell"><div class="footer-top"><a class="brand" href="{home}" aria-label="Zun Consulting トップページへ"><span class="brand-mark" aria-hidden="true">Z</span><span><span class="brand-word">ZUN CONSULTING</span><span class="brand-sub">経営支援・業務改善</span></span></a><nav class="footer-nav" aria-label="フッターナビゲーション">{links}</nav></div><div class="footer-bottom"><span>© 2026 Zun Consulting</span><span>開業準備中のご案内サイトです。</span></div></div></footer></body></html>'''

def label(index,name):return f'<div class="section-label"><span class="section-index">{index:02d} /</span><span class="eyebrow">{name}</span></div>'
def layout(title,desc,main,route=None):
    root=bool(route)
    return head(title,desc,root)+header(root,route)+f'<main id="main">{main}</main>'+footer(root)

def subhero(title,lede,crumb):
    return f'''<section class="page-hero"><div class="shell"><div class="breadcrumb"><a href="../index.html">ホーム</a> / {crumb}</div><h1>{title}</h1><p>{lede}</p></div></section>'''

home='''
<section class="hero" aria-labelledby="home-title">
<div class="hero-copy"><p class="hero-kicker eyebrow"><span class="rule" aria-hidden="true"></span>中小企業・小規模事業者の経営支援</p>
<h1 id="home-title">経営相談から、<br><em>実務の改善まで。</em></h1>
<p class="hero-lead">資金繰り、融資、補助金、事業計画、AIを使った業務改善。<br>会社の状況を整理し、取り組める方法を一緒に考えます。</p>
<a href="services/index.html" class="arrow-link">具体的な支援内容を見る</a>
</div><div class="hero-art hero-topics"><div class="topics-inner"><div class="topics-overline">予定している支援分野</div><div class="topics-heading">経営のことも、<br>日々の仕事のことも。</div><ul class="topic-list"><li><span>01</span><strong>経営改善・事業計画</strong></li><li><span>02</span><strong>資金繰り・融資</strong></li><li><span>03</span><strong>創業・補助金活用</strong></li><li><span>04</span><strong>AI・業務効率化</strong></li></ul><div class="topics-foot">現在、開業に向けて相談受付を準備しています。</div></div></div>
</section>
<div class="hero-bottom"><div class="shell hero-bottom-in"><span>経営相談の経験と、IT・AIの知見を組み合わせて支援します。</span><a href="about/index.html">担当者について <span aria-hidden="true">↗</span></a></div></div>
<section class="section statement" aria-labelledby="needs-title"><div class="shell statement-inner">'''+label(1,'相談のきっかけ')+'''<div><h2 id="needs-title" class="section-title">例えば、こんな相談から。</h2><div class="needs-list"><p>売上や利益が伸びず、どこから改善すべきか分からない。</p><p>資金繰りや返済が心配。借入れの前に状況を整理したい。</p><p>補助金の活用を考えているが、事業計画の作り方が分からない。</p><p>紙の書類や手入力が多い。AIやITで負担を減らしたい。</p></div><p class="needs-note">相談内容が整理できていない段階でも、現状を確認するところから考えます。</p></div></div></section>
<section class="section" aria-labelledby="services-title"><div class="shell"><div class="section-head">'''+label(2,'支援内容')+'''<div><h2 id="services-title" class="section-title">予定している支援内容</h2><p class="section-intro">制度の利用だけを目的にせず、経営上の課題に合う方法を検討します。</p></div></div>
<div class="service-rows">
<a class="service-row" href="services/index.html#management"><span class="service-no">01</span><span class="service-name">経営改善・<br>事業計画</span><span class="service-desc">経営課題の整理、売上・費用の検討、事業計画、設備投資の判断材料づくり。</span><span class="service-arrow" aria-hidden="true">↗</span></a>
<a class="service-row" href="services/index.html#finance"><span class="service-no">02</span><span class="service-name">資金繰り・<br>融資</span><span class="service-desc">資金繰りの見通し、借入れと返済の整理、融資を検討するための資料づくり。</span><span class="service-arrow" aria-hidden="true">↗</span></a>
<a class="service-row" href="services/index.html#startup"><span class="service-no">03</span><span class="service-name">創業・<br>補助金</span><span class="service-desc">創業計画、補助金制度の確認、申請に必要な事業内容・収支計画の整理。</span><span class="service-arrow" aria-hidden="true">↗</span></a>
<a class="service-row" href="services/index.html#digital"><span class="service-no">04</span><span class="service-name">AI・<br>業務改善</span><span class="service-desc">帳票の転記、書類管理、照合作業、社内情報の整理などの効率化。</span><span class="service-arrow" aria-hidden="true">↗</span></a>
</div><div class="services-more"><a class="arrow-link" href="services/index.html">支援内容を詳しく見る</a></div></div></section>
<section class="section cases" aria-labelledby="cases-title"><div class="shell"><div class="section-head">'''+label(3,'相談事例')+'''<div><h2 class="section-title" id="cases-title">実際にあった相談の例</h2><p class="section-intro">何を確認し、どんな対応を考えたか。守秘義務に配慮して、支援経験の一部を紹介します。</p></div></div>
<div class="case-grid">
<a href="cases/index.html#case-01" class="case-block feature"><div class="case-category">製造業 ／ 業務改善</div><span class="case-number" aria-hidden="true">01</span><h3 class="case-title">部品の照合ミスを減らしたい</h3><p class="case-teaser">AIで判定するより、Excelで照合ルールを決める方法を提案しました。</p><span class="case-read">事例を読む <span aria-hidden="true">↗</span></span></a>
<a href="cases/index.html#case-02" class="case-block"><div class="case-category">資金繰り ／ 融資相談</div><span class="case-number" aria-hidden="true">02</span><h3 class="case-title">融資の前に、入金の状況を確認</h3><p class="case-teaser">資金が足りない原因を調べ、未入金の確認から着手した事例です。</p><span class="case-read">事例を読む <span aria-hidden="true">↗</span></span></a>
<a href="cases/index.html#case-03" class="case-block"><div class="case-category">創業 ／ 事業計画</div><span class="case-number" aria-hidden="true">03</span><h3 class="case-title">貸別荘の計画を現地で整理</h3><p class="case-teaser">事業者と現地を確認し、計画の内容と伝え方を整えました。</p><span class="case-read">事例を読む <span aria-hidden="true">↗</span></span></a>
</div><div class="case-more"><a href="cases/index.html" class="arrow-link">相談事例をもっと見る</a></div></div></section>
<section class="section method" aria-labelledby="method-title"><div class="shell"><div class="section-head">'''+label(4,'支援の進め方')+'''<div><h2 class="section-title" id="method-title">相談から実行まで</h2><p class="section-intro">相談内容によって進め方は異なりますが、基本的には以下の順番で検討します。</p></div></div>
<div class="method-grid"><div class="method-step"><div class="method-num">01.</div><h3>相談内容を確認</h3><p>今困っていること、実現したいことを聞きます。</p></div><div class="method-step"><div class="method-num">02.</div><h3>現状を整理</h3><p>数字や資料、業務の流れなどを確認します。</p></div><div class="method-step"><div class="method-num">03.</div><h3>対応方法を検討</h3><p>費用や効果、実現可能性を比較します。</p></div><div class="method-step"><div class="method-num">04.</div><h3>実行を支援</h3><p>計画や書類、業務手順の整備につなげます。</p></div></div></div></section>
<section class="section about" aria-labelledby="about-title"><div class="shell"><div class="section-head">'''+label(5,'担当者について')+'''<div><h2 id="about-title" class="section-title">経営相談とIT・AIの両方に携わっています。</h2></div></div><div class="about-grid"><p class="about-lead">課題を整理し、<br>実行できる方法を<br>考えます。</p><div class="about-body"><p>地域の商工会で、中小企業・小規模事業者の経営相談に携わってきました。資金繰り、融資、創業、補助金、経営改善などの相談に加え、業務のデジタル化やAI活用にも取り組んでいます。</p><p>新しいシステムを使うこと自体を目的にはせず、費用や運用負担を考え、既存のソフトで十分ならその方法も検討します。</p><p class="about-note">Zun Consultingは開業準備中です。掲載内容は、これまでの経験と今後予定している支援分野についてのご案内です。</p><a href="about/index.html" class="arrow-link">担当者について詳しく</a></div></div></div></section>
<section class="contact-band" aria-labelledby="contact-home-title"><div class="shell contact-in"><div><h2 id="contact-home-title">相談受付について</h2><p>現在、開業に向けて相談窓口とサービス内容を準備しています。受付方法・料金などは確定後に掲載します。</p></div><a class="contact-cta" href="contact/index.html">受付状況を確認する</a></div></section>
'''
(ROOT/'index.html').write_text(layout('中小企業の経営相談・業務改善','資金繰り、融資、補助金、事業計画、AI・業務改善。地域の中小企業・小規模事業者の経営課題に取り組むZun Consultingの開業準備サイトです。',home),encoding='utf-8')

svc=subhero('支援内容','経営改善から資金繰り、補助金、AIを使った業務効率化まで。相談内容に応じて、必要な手段を組み合わせて検討します。','支援内容')+'''<div class="page-main"><div class="shell">
<section class="page-detail" id="management"><div class="detail-counter">01</div><div class="detail-body"><h2>経営改善・事業計画</h2><p>「売上はあるのに利益が残らない」「設備投資をしてよいか迷っている」。会社の現状と経営者の考えを整理し、取り組む順番や必要な計画を検討します。</p><div class="detail-sub"><div><h3>主な相談内容</h3><p>経営課題の整理、売上・費用の分析、経営改善計画、設備投資の検討、事業計画の作成。</p></div><div><h3>支援で整理すること</h3><p>課題の優先順位、改善案、収支の見通し、実行するための手順。</p></div></div></div></section>
<section class="page-detail" id="finance"><div class="detail-counter">02</div><div class="detail-body"><h2>資金繰り・融資</h2><p>借りるべきかどうかも含め、まず資金が不足する原因と時期を確認します。返済額や借入残高を整理し、必要な資金調達や対応方法を考えます。</p><div class="detail-sub"><div><h3>主な相談内容</h3><p>資金繰り表、借入先別の返済計画、融資に必要な資料、資金調達の選択肢。</p></div><div><h3>確認すること</h3><p>入金・支払時期、資金不足の要因、返済余力、調達コスト。</p></div></div></div></section>
<section class="page-detail" id="startup"><div class="detail-counter">03</div><div class="detail-body"><h2>創業・補助金</h2><p>創業の準備や、新しい事業を始めるときの計画づくり。補助金の利用が目的にならないよう、事業の必要性や資金計画から検討します。</p><div class="detail-sub"><div><h3>主な相談内容</h3><p>創業計画、事業計画、補助金制度の確認、必要書類や収支の整理。</p></div><div><h3>確認すること</h3><p>対象要件、申請期限・公募回、自己資金、採択後の実行条件。</p></div></div><p class="quiet">※補助金採択・融資実行を保証するものではありません。法令上の独占業務は有資格者の範囲を尊重します。</p></div></section>
<section class="page-detail" id="digital"><div class="detail-counter">04</div><div class="detail-body"><h2>AI・業務改善</h2><p>紙の書類の転記、繰り返し入力、照合、情報を探す時間など、日常業務の負担を減らす方法を検討します。AIだけでなく、Excelや既存ソフトによる改善も対象です。</p><div class="detail-sub"><div><h3>主な相談内容</h3><p>帳票処理、OCR、データ照合、PC・ブラウザ業務の自動化、情報共有、AI活用。</p></div><div><h3>判断の基準</h3><p>精度、導入費用、使いやすさ、情報管理、運用できる人員。</p></div></div></div></section>
<p class="notice">相談・サービスの受付開始前のご案内です。料金・具体的な提供範囲については、開業時に確定します。</p>
</div></div>'''
(ROOT/'services').mkdir(exist_ok=True)
(ROOT/'services/index.html').write_text(layout('支援内容','経営改善、資金繰り・融資、創業・補助金、AI・業務改善。Zun Consultingの対応予定分野を紹介します。',svc,'/services/'),encoding='utf-8')

cases=subhero('相談事例','これまでの相談で、何を確認し、どのように対応したか。個別の企業名や機密情報を除き、経験の範囲を明記して紹介します。','相談事例')+'''<div class="page-main"><div class="shell"><div class="case-list">
<article id="case-01" class="case-detail"><span class="status">支援経験</span><h2>部品の照合ミスを減らしたい</h2><div class="case-type">製造業 ／ 業務改善</div><p>部品の照合作業でミスが出るという相談。作業の流れと照合条件を確認した結果、AIによる推測よりも、Excelで決まった条件を照合する方法が適していると判断しました。</p><p class="result"><strong>対応：</strong>Excelによる照合方法を提案し、担当者の試作につながりました。実運用での効果は未確認です。</p></article>
<article id="case-02" class="case-detail"><span class="status">支援経験</span><h2>追加融資の前に、未入金を確認</h2><div class="case-type">資金繰り ／ 融資相談</div><p>資金不足に関する融資相談。入出金の状況を確認すると、行政からの売掛金の入金が遅れていました。追加借入れを前提とせず、まず担当部署への確認を促しました。</p><p class="result"><strong>対応：</strong>入金に関する支払対応につながりました。借入れの必要性を原因から考えた事例です。</p></article>
<article id="case-03" class="case-detail"><span class="status">支援経験</span><h2>貸別荘の事業計画を現地で整理</h2><div class="case-type">創業・補助金 ／ 事業計画</div><p>貸別荘の事業計画について、物件の現地確認を交えて事業者の構想を聞き、設備や立地の特徴を計画へ反映する方法を検討しました。</p><p class="result"><strong>対応：</strong>事業計画の整理を支援し、補助金採択につながりました。個別の結果であり、採択を保証するものではありません。</p></article>
<article class="case-detail"><span class="status">試作段階</span><h2>借入れと返済の状況を一覧化</h2><div class="case-type">経営管理 ／ 管理表の試作</div><p>金融機関ごとに分かれている借入れの残高や返済額、完済時期をまとめ、今後の資金負担を把握する管理表を試作しました。</p><p class="result"><strong>段階：</strong>試作。導入成果は確認していません。</p></article>
</div><p class="notice">事例は守秘義務に配慮して内容を一般化しています。特定の企業、支援時期、成果を識別できる情報は掲載していません。</p></div></div>'''
(ROOT/'cases').mkdir(exist_ok=True)
(ROOT/'cases/index.html').write_text(layout('相談事例','経営相談、融資、創業、AI・業務改善について、過去の相談事例と対応の到達点を紹介します。',cases,'/cases/'),encoding='utf-8')

about=subhero('担当者について','中小企業の経営相談と、実務のデジタル化の両方に取り組んできました。','担当者について')+'''<div class="page-main"><div class="shell prose"><h2>これまでに携わってきた業務</h2><p>地域の商工会で、中小企業・小規模事業者の相談支援に携わっています。資金繰り、融資、補助金、創業、経営改善、事業計画など、業種を問わず幅広い相談に対応してきました。</p><p>また、AIやソフトウェアを実際の業務に取り入れ、書類処理や情報整理、業務の自動化についても取り組んでいます。</p><div class="divider"></div><h2>支援するときに大切にしていること</h2><p>「補助金を使いたい」という相談でも、先に資金繰りや投資目的を整理した方がよい場合があります。「AIを導入したい」という相談でも、Excelの方が確実で安い場合があります。</p><p>最初から解決策を決めつけず、会社の状況と目的に合わせて、取り組める方法を選ぶことを大切にしています。</p><div class="divider"></div><h2>開業について</h2><p>Zun Consultingは現在、開業準備中です。正式な事業開始日、相談受付方法、料金については、確定後にお知らせします。</p><p class="quiet">※本ページの経歴は個人としての経験を示すものです。所属組織によるサービス提供・推薦を意味するものではありません。</p></div></div>'''
(ROOT/'about').mkdir(exist_ok=True)
(ROOT/'about/index.html').write_text(layout('担当者について','商工会での経営相談の実務経験と、IT・AIの活用を組み合わせた支援方針について紹介します。',about,'/about/'),encoding='utf-8')

contact=subhero('相談受付について','現在、独立開業に向けて準備を進めています。','相談受付について')+'''<div class="page-main"><div class="shell prose"><div class="contact-note"><h2>現在、相談受付の準備中です。</h2><p>正式な連絡先・相談方法・料金・提供条件は、事業開始前にこのページで案内します。現時点ではお問い合わせフォームを設置していません。</p></div><h2>相談開始後の流れ（予定）</h2><div class="contact-flow"><div><strong>01</strong><span>相談内容をお知らせいただく</span></div><div><strong>02</strong><span>現状や必要な資料を確認する</span></div><div><strong>03</strong><span>支援範囲と費用を確認して進める</span></div></div><p class="quiet">個人情報や企業の機密資料を、このページから送信する必要はありません。</p><div class="back-link"><a href="../index.html">トップページへ戻る</a></div></div></div>'''
(ROOT/'contact').mkdir(exist_ok=True)
(ROOT/'contact/index.html').write_text(layout('相談受付について','Zun Consultingの相談受付状況と、今後の相談方法・料金についてのご案内です。',contact,'/contact/'),encoding='utf-8')

# Preserve the original editorial design foundation and extend it selectively.
css_path=ROOT/'assets/style.css'
old_css=css_path.read_text(encoding='utf-8')
old_css=old_css.split('/* TRUST-FIRST REFINEMENTS */')[0]
css_path.write_text(old_css+'''\n/* TRUST-FIRST REFINEMENTS */
/* Reuse the refined ivory/forest typography, without fabricated visual diagrams or abstract slogans. */
.header .brand-sub,.footer .brand-sub{font-family:var(--ui);font-size:10px;letter-spacing:.13em}
.nav .nav-contact::after{content:'↗'}
.hero{grid-template-columns:minmax(0,57%) minmax(0,43%);min-height:655px}
.hero-copy{padding-top:clamp(88px,10vw,151px);padding-bottom:80px}
.hero-kicker{font-family:var(--ui);font-size:12px;letter-spacing:.08em;margin-bottom:55px}
.hero h1{font-size:clamp(42px,4.7vw,73px);letter-spacing:-.065em;line-height:1.55}
.hero h1 em{white-space:nowrap}
.hero-lead{font-size:15px;line-height:2.15;max-width:560px}
.hero-topics{min-height:655px;display:flex;align-items:center;background:#192c29;color:#faf8f0;padding:67px clamp(30px,4vw,72px);border-left:1px solid #30433d}
.topics-inner{width:100%;max-width:560px;margin:auto}
.topics-overline{font-size:12px;color:#c3d0c8;letter-spacing:.15em;border-bottom:1px solid #65756d;padding:0 0 17px}
.topics-heading{font-family:var(--display);font-size:clamp(28px,2.6vw,39px);font-weight:500;line-height:1.7;letter-spacing:-.055em;margin:43px 0 39px}
.topic-list{padding:0;margin:0;list-style:none;border-top:1px solid #697a70}
.topic-list li{display:flex;gap:24px;align-items:baseline;border-bottom:1px solid #53685d;padding:19px 0 21px}
.topic-list li span{font:italic 16px Georgia,serif;color:#d09b7c;min-width:25px}
.topic-list li strong{font-family:var(--display);font-size:clamp(19px,1.7vw,27px);font-weight:500;letter-spacing:-.02em}
.topics-foot{font-size:11px;line-height:1.9;color:#aebbb3;margin-top:34px}
.hero-bottom-in{font-size:12px;min-height:72px}.hero-bottom-in a{color:var(--ink);font-weight:600;text-decoration:none}.hero-bottom-in a span{color:var(--rust);padding-left:8px}
.section{padding:108px 0}
.section-head{margin-bottom:48px}.section-title{font-size:clamp(33px,3.4vw,53px)}
.eyebrow{font-family:var(--ui);letter-spacing:.075em;font-weight:600;font-size:12px}
.needs-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 39px;margin-top:40px;border-top:1px solid var(--line)}
.needs-list p{position:relative;border-bottom:1px solid var(--line);margin:0;padding:23px 9px 26px 25px;color:var(--ink-soft);line-height:1.95}
.needs-list p::before{content:'';position:absolute;top:34px;left:3px;width:6px;height:6px;border:1px solid var(--rust);border-radius:50%}
.needs-note{margin-top:27px;color:var(--muted);font-size:13px}
.service-row{grid-template-columns:7% 31% 1fr 5%;padding:33px 5px 36px}.service-name{font-size:clamp(23px,2.2vw,32px)}
.case-grid{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);grid-template-rows:repeat(2,minmax(240px,1fr))}
.case-block{min-height:auto;padding:31px 37px;overflow:hidden}.case-block.feature{grid-row:1 / 3;min-height:490px;justify-content:flex-end}
.case-number{font-size:36px;line-height:1;margin:12px 0 15px}.feature .case-number{font-size:61px;margin:auto 0 25px}
.case-title{font-size:clamp(22px,2vw,29px);line-height:1.5;margin:0 0 13px}.case-teaser{font-size:12px;line-height:1.9;margin:0}.case-read{font-size:11px;font-weight:700;letter-spacing:.06em;margin-top:24px;display:inline-flex;gap:16px;align-items:center}
.case-category{font-size:11px;letter-spacing:.04em;margin:0 0 13px}
.method-step{min-height:242px}.method-step h3{font-size:22px;margin:30px 0 13px}.method-step p{font-size:13px}
.about-note{font-size:12px!important;line-height:2!important;margin-bottom:25px!important}
.about-body .arrow-link{margin-top:12px}.contact-band h2{font-size:clamp(32px,3.8vw,50px);margin-top:0}
.contact-flow{border-top:1px solid var(--line);margin:30px 0 40px}.contact-flow div{display:flex;align-items:center;gap:23px;border-bottom:1px solid var(--line);padding:22px 5px}.contact-flow strong{font:italic 20px Georgia,serif;color:var(--rust)}
.page-hero{padding:82px 0 78px}.page-hero h1{font-size:clamp(43px,4.5vw,66px);margin:10px 0 15px}.page-main{padding:70px 0 98px}.page-detail{scroll-margin-top:24px}
.case-detail{scroll-margin-top:24px}
@media(max-width:1000px){.hero{min-height:575px}.hero-copy{padding:88px 32px 65px}.hero h1{font-size:clamp(42px,5vw,60px)}.hero-topics{min-height:575px;padding:46px 33px}.topics-heading{font-size:31px}.topic-list li{gap:14px;padding:16px 0}.topic-list li strong{font-size:19px}.section{padding:95px 0}}
@media(max-width:760px){.hero{min-height:unset;display:flex;flex-direction:column}.hero-copy{padding:55px 20px 66px}.hero-kicker{font-size:10px;letter-spacing:.07em;margin-bottom:32px}.hero h1{font-size:clamp(35px,8.7vw,57px);white-space:normal;line-height:1.55}.hero-lead{font-size:13px}.hero-lead br{display:none}.hero-topics{min-height:unset;padding:47px 24px 53px}.topics-heading{font-size:28px;margin:30px 0}.topic-list li{padding:16px 0}.topic-list li strong{font-size:22px}.topics-foot{margin-top:22px}.hero-bottom-in{gap:13px}.section{padding:75px 0}.section-head{margin-bottom:31px}.needs-list{grid-template-columns:1fr;gap:0;margin-top:25px}.needs-list p{font-size:13px;padding:19px 4px 20px 25px}.needs-list p::before{top:31px}.needs-note{font-size:12px}.case-grid{grid-template-columns:1fr;grid-template-rows:auto}.case-block,.case-block.feature{min-height:250px;grid-row:auto}.case-block.feature{min-height:310px}.case-block{padding:27px 27px 31px}.feature .case-number{font-size:45px;margin:15px 0 22px}.case-number{font-size:32px}.method-step{min-height:210px}.method-step h3{font-size:18px;margin:23px 0 10px}.method-step p{font-size:11px}.about-lead{font-size:30px}.page-hero{padding:56px 0 62px}.page-hero h1{font-size:42px}.page-main{padding:54px 0 85px}}
@media(max-width:390px){.hero h1{font-size:34px}.topics-heading{font-size:26px}.topic-list li strong{font-size:20px}.method-step h3{font-size:16px}}
''',encoding='utf-8')
(ROOT/'robots.txt').write_text('User-agent: *\nDisallow: /\n',encoding='utf-8')
(ROOT/'sitemap.xml').write_text('''<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'''+''.join('<url><loc>'+SITE+route+'</loc></url>' for route in ('','services/','cases/','about/','contact/'))+'</urlset>',encoding='utf-8')
(ROOT/'README.md').write_text('''# Zun Consulting Website (v4)\n\n初期案の深緑・生成り・明朝体と左右分割のビジュアルを維持しつつ、AI的な抽象コピー・英語装飾・架空の資料イラストを廃止。\n\n- `index.html` トップ\n- `services/index.html` 支援内容\n- `cases/index.html` 相談事例（到達点と未確認事項を分離）\n- `about/index.html` 担当者について\n- `contact/index.html` 相談受付について\n- `assets/style.css` アクセシブルなレスポンシブスタイル\n- `assets/main.js` モバイルメニュー\n\n開業準備中のため、全ページ noindex/nofollow、robots.txt でインデックスを抑止。連絡先・料金など未確認情報は掲載しない。公開前に本人情報・事例公開の同意範囲・利益相反を確認。\n\n`python build_site.py` で共通ヘッダーとページ本文を再生成します。特別なビルド依存は不要です。\n''',encoding='utf-8')
# Remove prior AI-like illustrated assets from deployable site.
for name in ('assets/hero-art.svg','assets/og.png','assets/og.svg'):
    f=ROOT/name
    if f.exists():f.unlink()
# Keep old paths functional, redirecting to the current path names.
for old,new in (('service','services'),('approach','about')):
    p=ROOT/old/'index.html'
    p.write_text(f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url=../{new}/"><title>移動しました | Zun Consulting</title></head><body><p>ページは<a href="../{new}/">こちら</a>へ移動しました。</p></body></html>',encoding='utf-8')
print('Built v4 pages')
