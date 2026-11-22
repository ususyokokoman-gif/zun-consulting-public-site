"""Dependency-free static site builder: python build.py (from repo root)."""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parent
SITE_URL='https://ususyokokoman-gif.github.io/zun-consulting-public-site/'

NAV=[('service/index.html','支援領域'),('cases/index.html','支援の考え方と事例'),('approach/index.html','私たちの姿勢'),('contact/index.html','お問い合わせ')]

def layout(body,title,description,section='',depth=0):
    prefix='../'*depth
    nav_links=[]
    for href,label in NAV:
        active=' aria-current="page"' if href.split('/')[0]==section else ''
        nav_links.append(f'<a href="{prefix}{href}"{active}>{label}</a>')
    nav_links[-1]=nav_links[-1].replace('>お問い合わせ',' class="nav-contact">お問い合わせ')
    canonical=SITE_URL+section+('/' if section else '')
    return f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | Zun Consulting</title>
<meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#192827"><meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{canonical}"><link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg">
<link rel="stylesheet" href="{prefix}assets/style.css">
<meta property="og:type" content="website"><meta property="og:locale" content="ja_JP"><meta property="og:title" content="{escape(title)} | Zun Consulting">
<meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE_URL}assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<script defer src="{prefix}assets/main.js"></script>
</head><body>
<a class="skip-link" href="#main">本文へ移動</a>
<header class="header"><div class="header-in shell">
<a class="brand" href="{prefix}index.html" aria-label="Zun Consulting トップページへ"><span class="brand-mark" aria-hidden="true">Z</span><span><span class="brand-word">ZUN CONSULTING</span><span class="brand-sub">BUSINESS ADVISORY &amp; IMPLEMENTATION</span></span></a>
<button class="menu-button" type="button" aria-label="メニューを開閉" aria-expanded="false" aria-controls="primary-nav"><span aria-hidden="true"></span></button>
<nav id="primary-nav" class="nav" aria-label="グローバルナビゲーション">{''.join(nav_links)}</nav>
</div></header>
<main id="main">{body}</main>
<footer class="footer"><div class="shell"><div class="footer-top">
<a class="brand" href="{prefix}index.html" aria-label="Zun Consulting トップページへ"><span class="brand-mark" aria-hidden="true">Z</span><span><span class="brand-word">ZUN CONSULTING</span><span class="brand-sub">BUSINESS ADVISORY &amp; IMPLEMENTATION</span></span></a>
<nav class="footer-nav" aria-label="フッターナビゲーション"><a href="{prefix}service/index.html">支援領域</a><a href="{prefix}cases/index.html">事例</a><a href="{prefix}approach/index.html">私たちの姿勢</a><a href="{prefix}contact/index.html">お問い合わせ</a></nav></div>
<div class="footer-bottom"><span>© {2026} Zun Consulting. All rights reserved.</span><span>中小企業の判断と実行を支える。</span></div></div></footer>
</body></html>'''


def page_hero(label,title,lead):
    return f'''<section class="page-hero"><div class="shell"><div class="breadcrumb"><a href="../index.html">HOME</a> &nbsp;/&nbsp; {escape(title)}</div><div class="eyebrow">{label}</div><h1>{title}</h1><p>{lead}</p></div></section>'''

home='''
<section class="hero" aria-labelledby="home-title">
<div class="hero-copy"><p class="hero-kicker eyebrow"><span class="rule" aria-hidden="true"></span>THE BUSINESS DECISION PARTNER</p>
<h1 id="home-title">判断を、<br><em>前進</em>に変える。</h1>
<p class="hero-lead">経営の課題を整理し、選ぶべき道筋を明確にする。<br>資金繰りから事業計画、AI・業務改善まで。<br>考えるだけで終わらない、実行につながる支援を。</p>
<a href="service/" class="arrow-link">支援できることを見る</a></div>
<div class="hero-art" role="img" aria-label="課題の整理、判断、実行を描いたZun Consultingオリジナルの意思決定ノート"><svg aria-hidden="true"><image href="assets/hero-art.svg" width="100%" height="100%" preserveAspectRatio="xMidYMid slice"/></svg><span class="art-label">01 / FROM QUESTION<br>TO NEXT ACTION</span></div>
</section>
<div class="hero-bottom"><div class="shell hero-bottom-in"><span class="eyebrow">THINK — DECIDE — DO</span><div class="series"><span><strong>01</strong> 論点を整理する</span><span><strong>02</strong> 判断材料をつくる</span><span><strong>03</strong> 実行へつなげる</span></div></div></div>
<section class="section statement" aria-labelledby="statement-title"><div class="shell statement-inner">
<div class="section-label"><span class="section-index">01 /</span><span class="eyebrow">OUR POINT OF VIEW</span></div>
<div><h2 id="statement-title" class="statement-quote">必要なのは、<br>正解らしい答えより、<br><b>納得して動ける判断。</b></h2>
<div class="statement-copy"><p>経営の悩みは、一つの専門分野に収まりません。売上や資金繰りの問題が、業務の流れや人手不足につながっていることもあります。</p><p>最初から解決策を決めつけず、現場と数字、経営者の考えを一緒に見ます。課題をほどき、優先順位を決め、実行できる形まで整えることを大切にしています。</p></div></div></div></section>
<section class="section" aria-labelledby="services-title"><div class="shell"><div class="section-head"><div class="section-label"><span class="section-index">02 /</span><span class="eyebrow">WHAT WE DO</span></div><div><h2 id="services-title" class="section-title">課題ごとに、<br>最適な手段を選ぶ。</h2><p class="section-intro">制度の知識だけでも、AIの技術だけでも、経営は変わりません。分野を横断しながら、必要な支援を組み合わせます。</p></div></div>
<div class="service-rows">
<a class="service-row" href="service/#business"><span class="service-no">01</span><span class="service-name">経営判断・<br>事業計画</span><span class="service-desc">散らばった悩みを整理し、経営者が判断できる材料へ。事業の方向性、設備投資、創業、改善計画を具体化します。</span><span class="service-arrow">↗</span></a>
<a class="service-row" href="service/#finance"><span class="service-no">02</span><span class="service-name">資金繰り・<br>制度活用</span><span class="service-desc">融資を受ける前に本当の資金課題を把握。返済計画、補助金、税制優遇など、目的と条件に合う選択肢を検討します。</span><span class="service-arrow">↗</span></a>
<a class="service-row" href="service/#digital"><span class="service-no">03</span><span class="service-name">AI・<br>業務改善</span><span class="service-desc">手入力、書類管理、照合、情報共有などの負担を減らす。AIありきではなく、現場に残る仕組みをつくります。</span><span class="service-arrow">↗</span></a>
</div><div class="services-more"><a class="arrow-link" href="service/">すべての支援領域</a></div>
</div></section>
<section class="section cases" aria-labelledby="case-title"><div class="shell"><div class="section-head"><div class="section-label"><span class="section-index">03 /</span><span class="eyebrow">SELECTED STORIES</span></div><div><h2 class="section-title" id="case-title">課題を見直すと、<br>答えも変わる。</h2><p class="section-intro cases-intro">成果を大きく見せるための事例ではありません。「何を問題として捉え、どう判断したか」に焦点を当てた、現場での支援エピソードです。</p></div></div>
<div class="case-grid">
<a href="cases/#case-01" class="case-block feature"><div class="case-category">製造業 / 支援経験</div><div class="case-number">01.</div><h3 class="case-title">AIよりも、<br>Excelが正しかった。</h3><p class="case-teaser">部品の照合ミス。技術から考えず、作業と判定ルールから解決策を探しました。</p></a>
<a href="cases/#case-02" class="case-block"><div class="case-category">資金繰り / 支援経験</div><div class="case-number">02.</div><h3 class="case-title">借りる前に、<br>入金を確かめる。</h3><p class="case-teaser">融資相談の背景にあった入金遅延。まず原因を確認することで対応が変わりました。</p></a>
<a href="cases/#case-03" class="case-block"><div class="case-category">創業・補助金 / 支援経験</div><div class="case-number">03.</div><h3 class="case-title">構想を、<br>伝わる計画に。</h3><p class="case-teaser">現地で事業者の考えを聞き、事業計画の伝え方から見直しました。</p></a>
</div><div class="case-more"><a href="cases/" class="arrow-link">ほかの事例・試作も見る</a></div></div></section>
<section class="section method" aria-labelledby="method-title"><div class="shell"><div class="section-head"><div class="section-label"><span class="section-index">04 /</span><span class="eyebrow">HOW WE WORK</span></div><div><h2 id="method-title" class="section-title">答えを急がない。<br>実行は止めない。</h2><p class="section-intro">相談から解決までの道筋は、案件ごとに変わります。変わらないのは、現実に使える判断を一緒につくる姿勢です。</p></div></div>
<div class="method-grid"><div class="method-step"><div class="method-num">01.</div><h3>聴く</h3><p>経営者が実現したいことと、現場で起きていることを把握する。</p></div><div class="method-step"><div class="method-num">02.</div><h3>ほどく</h3><p>問題を分け、数字や資料を確認し、原因と優先順位を整理する。</p></div><div class="method-step"><div class="method-num">03.</div><h3>決める</h3><p>費用・効果・リスクを比較し、納得して選べる選択肢をつくる。</p></div><div class="method-step"><div class="method-num">04.</div><h3>動かす</h3><p>計画や書類、業務の仕組みに落とし込み、実行を支える。</p></div></div><div class="method-bottom"><a href="approach/" class="arrow-link">支援の考え方を詳しく</a></div></div></section>
<section class="section about" aria-labelledby="about-title"><div class="shell"><div class="section-head"><div class="section-label"><span class="section-index">05 /</span><span class="eyebrow">WHY ZUN</span></div><div><h2 id="about-title" class="section-title">経営の現場と、<br>技術の両方から。</h2></div></div><div class="about-grid"><p class="about-lead">「何をするか」の前に、<br>「なぜするか」を<br>確かめる。</p><div class="about-body"><p>中小企業・小規模事業者の経営相談で培った視点と、IT・AIによる業務改善の知見を組み合わせます。融資や補助金の相談から見えてくる問題もあれば、日々の書類作業から経営全体の課題が見えることもあります。</p><p>複数の領域をつなぎ、判断のための資料づくりから具体的な実装まで支える。経営者の隣で考え、動く立場を目指しています。</p><div class="about-note">※ Zun Consultingは事業準備中です。サービス提供条件・相談窓口は確定後にご案内します。</div></div></div></div></section>
<section class="contact-band" aria-labelledby="contact-home-title"><div class="shell contact-in"><div><div class="eyebrow">START WITH ONE QUESTION</div><h2 id="contact-home-title">まずは、目の前の<br>一つの課題から。</h2><p>ご相談の受付体制は現在準備中です。受付開始については、お問い合わせページでお知らせします。</p></div><a class="contact-cta" href="contact/">受付状況を見る</a></div></section>
'''

service=page_hero('EXPERTISE / 01','支援領域','経営の課題は、ひとつの分野では完結しません。全体を見ながら、いま必要な支援を組み合わせ、判断と実行につなげます。')+'''
<div class="shell page-main">
<section class="page-detail" id="business"><div class="detail-counter">01 / ADVISORY</div><div class="detail-body"><h2>経営判断・事業計画</h2><p>「やりたいことはあるが、優先順位が決まらない」「設備投資を進めてよいか迷っている」。そのような段階から、論点を明確にし、判断材料を整理します。</p><div class="detail-sub"><div><h3>主な支援テーマ</h3><p>経営課題の整理／事業計画／創業準備／設備投資の検討／経営改善／実行計画</p></div><div><h3>目指す成果物</h3><p>経営者が判断できる選択肢、優先順位、収支の見通し、実行まで落とし込んだ計画。</p></div></div></div></section>
<section class="page-detail" id="finance"><div class="detail-counter">02 / FINANCE</div><div class="detail-body"><h2>資金繰り・融資・制度活用</h2><p>融資や補助金は、経営課題を解決するための手段です。制度への申請ありきではなく、必要な資金・投資の目的・返済への影響を踏まえて考えます。</p><div class="detail-sub"><div><h3>主な支援テーマ</h3><p>資金繰りの整理／借入返済の見える化／融資計画／補助金制度の検討／優遇税制の情報整理。</p></div><div><h3>支援時の原則</h3><p>制度の適用時点・公募回・要件を確認し、採択や融資実行などの結果を保証しません。独占業務は資格者の担当範囲を尊重します。</p></div></div></div></section>
<section class="page-detail" id="digital"><div class="detail-counter">03 / IMPLEMENTATION</div><div class="detail-body"><h2>AI・業務改善・デジタル化</h2><p>「手で転記する作業をなくしたい」「情報を探す時間を減らしたい」。日常業務の負担を観察し、必要ならAI、既存ソフト、自動化を組み合わせ、扱える形にします。</p><div class="detail-sub"><div><h3>主な支援テーマ</h3><p>帳票処理／OCR／データ照合／ブラウザ・PC業務の自動化／情報共有／AI活用／Web・発信の改善。</p></div><div><h3>導入判断の基準</h3><p>精度、費用、運用負担、情報管理、安全性。AIを使わない方がよい場合は、その方法を選びます。</p></div></div></div></section>
<div class="notice">※掲載内容は提供予定の支援領域です。個別の受任可否・契約条件・料金は未確定です。</div>
<div class="back-link"><a href="../">← トップページに戻る</a></div></div>'''

cases=page_hero('STORIES / 02','支援の考え方と事例','同じ課題でも、最適な答えは現場によって異なります。具体的な相談や検討の経緯を、結果の段階を区別して紹介します。')+'''
<div class="shell page-main"><div class="case-list">
<article class="case-detail" id="case-01"><div class="case-type">製造業 / 部品照合</div><div class="status">支援経験・試作提案</div><h2>AIよりも、Excelが正しかった。</h2><p>部品の照合ミスを減らしたいという相談。作業の流れと判定ルールを確認すると、AIの推測よりも決まった条件で照合できる表計算の仕組みが適していました。</p><p class="result"><strong>対応の到達点：</strong> Excelを使った方法を提案し、担当者による試作につながりました。現場への本導入や削減効果は確認されていません。</p></article>
<article class="case-detail" id="case-02"><div class="case-type">資金繰り / 入金遅延</div><div class="status">支援経験</div><h2>借りる前に、入金を確かめる。</h2><p>追加融資の相談を受けた際、資金不足の原因を確認。行政からの売掛金の入金が遅れている状況が分かり、まず担当部署への確認を促しました。</p><p class="result"><strong>対応の到達点：</strong> 支払対応につながりました。融資を前提とせず、原因の確認から着手した事例です。</p></article>
<article class="case-detail" id="case-03"><div class="case-type">創業・補助金 / 宿泊業</div><div class="status">支援経験</div><h2>構想を、伝わる計画に。</h2><p>貸別荘の事業計画について、物件を実際に見ながら事業者の構想を確認。現地でしか分からない魅力や前提条件を踏まえ、事業計画の伝え方を整理しました。</p><p class="result"><strong>対応の到達点：</strong> 補助金採択につながりました。採択は個別事例の結果であり、将来の採択を保証するものではありません。</p></article>
<article class="case-detail" id="case-04"><div class="case-type">経営管理 / 借入返済</div><div class="status">ツール試作</div><h2>数字の先を見えるようにする。</h2><p>金融機関ごとに分かれた借入情報を整理し、毎月の返済負担や完済時期を把握しやすくするための管理表を試作。</p><p class="result"><strong>対応の到達点：</strong> 試作段階です。実運用での導入成果は掲載していません。</p></article>
<article class="case-detail" id="case-05"><div class="case-type">小売・飲食 / 注文管理</div><div class="status">検討段階</div><h2>今の接客を壊さず、負担を減らす。</h2><p>InstagramのDMによる注文方法を変えずに、予約内容の整理や在庫確認、返信作業を省力化できないか検討しています。</p><p class="result"><strong>対応の到達点：</strong> 構想・検討段階です。導入実績はありません。</p></article>
<article class="case-detail" id="case-06"><div class="case-type">団体業務 / 情報共有</div><div class="status">構想段階</div><h2>普段の連絡を、もしもの備えに。</h2><p>LINE公式アカウントを通常の会員連絡に使い、災害時の連絡や状況把握にも活用できる仕組みを構想。</p><p class="result"><strong>対応の到達点：</strong> アイデアの段階です。サービスとしての提供・検証は行っていません。</p></article>
</div><div class="notice">※守秘義務に配慮し、企業名・個人名・非公開の数字は掲載していません。実施済みの支援、試作、構想は明示的に区別しています。</div><div class="back-link"><a href="../">← トップページに戻る</a></div></div>'''

approach=page_hero('PHILOSOPHY / 03','私たちの姿勢','経営者の隣に立つ支援とは何か。手段に飛びつく前に、考え方と仕事の進め方を定めています。')+'''
<div class="shell page-main"><div class="prose"><p class="big">社長が本当に決めたいことは、最初の相談内容と違うことがあります。</p><div class="divider"></div><h2>「何が問題か」から一緒に考える。</h2><p>「補助金を使いたい」と聞いても、最初から申請書を書き始めるとは限りません。なぜ投資するのか、資金が必要なのはいつか、事業として成り立つのか。経営の問いを整理することが、結果的に手戻りを減らします。</p><h2>技術ではなく、現場から選ぶ。</h2><p>AIは強力な道具ですが、万能ではありません。精度の保証が難しい判断にはルールベースの照合が適することも、複雑なシステムよりExcelが長く使えることもあります。導入後に現場の人が使えるかどうかまで考えます。</p><h2>判断できる資料と、動ける仕組みを。</h2><p>よい説明をするだけではなく、選択肢・根拠・費用・リスクを比較できる形にまとめます。決定した後は、計画・帳票・手順・デジタルツールへ具体化し、仕事として進められる状態を目指します。</p><h2>必要な専門性につなぐ。</h2><p>税務申告や法律判断など、資格・権限が必要な業務は、それぞれの専門家の領域を尊重します。複数の課題が絡むからこそ、役割を明確にし、経営者にとって全体が分かる支援を大切にします。</p><div class="divider"></div><p class="big">経営を動かすのは、流行の手法ではなく、納得できる判断と、その次の一歩です。</p><div class="back-link"><a href="../">← トップページに戻る</a></div></div></div>'''

contact=page_hero('CONTACT / 04','お問い合わせ','相談の入り口は、難しい事業計画でなくて構いません。日々の仕事で感じる一つの困りごとから、課題を整理していくことを目指しています。')+'''
<div class="shell page-main"><div class="prose"><div class="contact-note"><div class="eyebrow" style="color:#a65f3c;margin-bottom:16px">CURRENT STATUS</div><h2>相談受付は準備中です。</h2><p>現在、正式なお問い合わせ窓口とサービス提供条件を整備しています。受付開始後、こちらのページにご案内を掲載します。</p></div><h2>ご相談いただくことを想定しているテーマ</h2><p>業務を効率化したい、資金繰りの見通しを整理したい、設備投資の妥当性を確かめたい、補助金・事業計画について考えたい、AIをどう使うべきか検討したい――など。</p><p class="quiet">※このページには入力フォームや送信機能はありません。窓口の準備完了前に個人情報を送信する必要はありません。</p><div class="back-link"><a href="../">← トップページに戻る</a></div></div></div>'''

pages=[('index.html',home,'判断を、前進に変える。','Zun Consulting。中小企業の課題整理から経営判断、資金繰り・事業計画、AI・業務改善の実行まで、経営者の隣で考える支援。','',0),('service/index.html',service,'支援領域','経営判断・事業計画、資金繰り・融資・補助金・優遇税制、AI・業務改善。Zun Consultingの支援領域を紹介します。','service',1),('cases/index.html',cases,'支援の考え方と事例','製造業の部品照合、資金繰り、事業計画など、課題をどのように整理し判断したか。実績と試作・構想を分けて紹介。','cases',1),('approach/index.html',approach,'私たちの姿勢','解決策を決めつけず、現場と経営者の考えを確認する。Zun Consultingが大切にする課題整理・判断・実行の考え方。','approach',1),('contact/index.html',contact,'お問い合わせ','Zun Consultingのお問い合わせ・相談受付に関するご案内。現在、受付体制を準備中です。','contact',1)]
for dest,body,title,description,section,depth in pages:
    for folder in ('service','cases','approach','contact'):
        body=body.replace(f'href="{folder}/#',f'href="{folder}/index.html#')
        body=body.replace(f'href="{folder}/"',f'href="{folder}/index.html"')
    body=body.replace('href="../"','href="../index.html"')
    p=ROOT/dest
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(layout(body,title,description,section,depth),encoding='utf-8')

paths=['','service/','cases/','approach/','contact/']
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f' <url><loc>{SITE_URL}{p}</loc></url>\n' for p in paths)+'</urlset>\n',encoding='utf-8')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+SITE_URL+'sitemap.xml\n',encoding='utf-8')
print(f'Generated {len(pages)} pages')
