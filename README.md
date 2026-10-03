# OSWE Field Manual

OSWE / WEB-300 に必要な実践力を、Web Security Academy、コードリーディング、Exploit 開発を通して積み上げるための学習用リポジトリです。

## 目標

未知の Web アプリケーションを渡されたときに、次の流れを自力で進められる状態を目指します。

1. フレームワークとリクエスト処理の流れを理解する
2. 攻撃者が制御できる入力を追跡する
3. 脆弱な処理を特定する
4. 脆弱性を悪用可能な primitive に変換する
5. 必要なら複数の primitive を組み合わせる
6. Python PoC で再現する

## 学習ループ

```text
学習 / コードリーディング
    ↓
Web Security Academy / Reading Drill
    ↓
AIに答えを出させず自分で分析
    ↓
手動でExploit
    ↓
Python PoC
    ↓
再利用できる知識を抽出
    ↓
このリポジトリへ反映
```

最初から完全な百科事典は作りません。
実際に学習中に遭遇した内容から少しずつ育てます。

## 構成

```text
docs/
  methodology/          ホワイトボックス診断の方法論
  vulnerabilities/      脆弱性ごとの再利用可能な知識
  languages/            セキュリティ観点の言語・フレームワークメモ

web-security-academy/   各Labの記録とPython PoC
snippets/               再利用可能な小さなコード片
boilerplates/           汎用Exploit雛形
```

当面は Web Security Academy の各 Lab を解きながら `requests` を学びます。最初の Python PoC は自分で書き、次の Lab からは自作の過去コードをコピーして必要な処理を書き替えます。[進め方](docs/methodology/poc-writing.md)と [Requests チートシート](docs/methodology/requests-cheatsheet.md)を参照してください。

PoC 作成の実例は [Exploit Writing for OSWE](https://github.com/rizemon/exploit-writing-for-oswe) を主な参考にします。API の正確な動作は [Requests 公式資料](https://requests.readthedocs.io/en/latest/user/quickstart/)、試験要件は [OffSec 公式ガイド](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)で確認します。

## AI利用ルール

AIは、リファレンス整理、解答後の概念説明、自作コードのレビュー、再利用ノートの整理には使ってよいものとします。

一方、Labや演習の初回挑戦中は、AIに脆弱性箇所・payload・完成Exploitを直接出させません。

## 現在の重点分野

1. XSS
2. SQL Injection
3. Command Injection
4. File Upload
5. Path Traversal
6. SSRF
7. XXE
8. SSTI
9. CSRF / JWT / Authentication

一通り基礎を回したら、WEB-300 のモジュールと White-box Challenge Lab へ進みます。
