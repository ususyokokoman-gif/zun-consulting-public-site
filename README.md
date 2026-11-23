# Zun Consulting Website (v4)

初期案の深緑・生成り・明朝体と左右分割のビジュアルを維持しつつ、AI的な抽象コピー・英語装飾・架空の資料イラストを廃止。

- `index.html` トップ
- `services/index.html` 支援内容
- `cases/index.html` 相談事例（到達点と未確認事項を分離）
- `about/index.html` 担当者について
- `contact/index.html` 相談受付について
- `assets/style.css` アクセシブルなレスポンシブスタイル
- `assets/main.js` モバイルメニュー

開業準備中のため、全ページ noindex/nofollow、robots.txt でインデックスを抑止。連絡先・料金など未確認情報は掲載しない。公開前に本人情報・事例公開の同意範囲・利益相反を確認。

`python build_site.py` で共通ヘッダーとページ本文を再生成します。特別なビルド依存は不要です。
