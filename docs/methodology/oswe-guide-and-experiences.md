# OSWE 試験ガイドと合格体験記から見る PoC 練習

確認日: 2026-10-03。**試験要件は OffSec の現行ガイドを優先**する。以下の受験記は本人の経験であり、対象数、配点、試験環境や推奨実装の固定ルールを示すものではない。

## 公式要件

- [OSWE Exam Guide（2026-07-01 更新）](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide) は、実技 47 時間 45 分、終了後の文書提出 24 時間、合格点 85/100 としている。対象ごとの具体的な目的と点数は試験開始後の Exam Control Panel で示される。
- 同ガイドの *Exam Proofs* は、**各対象マシンの複数の脆弱性を悪用する、機能するスクリプト 1 本**を要求する。採点者による実行中の手作業は不要でなければならない。一方、実行前の netcat リスナーや Web サーバーの準備は許容される。リバースシェルを得た場合は実行後のフラグ取得などを手動で行えるが、シェルを得ない場合は PoC が proof 値を自動抽出する必要がある。[出典](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)
- レポートには攻撃の全手順、コマンド、出力、独自 Exploit のソースコードを含め、技術者が再現できる程度に記述する。提出するアーカイブには PDF のみを入れ、PoC は PDF 内にテキスト（平文または base64）として記載する。[出典](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)
- 試験中、AI チャットボット／LLM、SQLmap などの自動 Exploit ツール、ソースコードアナライザー、大規模脆弱性スキャナーは使用禁止。[OSWE Exam Guide](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)。[OSWE Exam FAQ（2025-12-15 更新）](https://help.offsec.com/hc/en-us/articles/360046418812-OSWE-Exam-FAQ) は、試験をオープンブックとし、ノートやオンライン資料は利用可能だが、AI チャットボット／直接プロンプト可能な LLM と試験内容について他者に助けを求める行為を除外している。

## 本人が書いた受験記から得られる練習上の示唆

| 受験記 | 確認した経験と示唆 |
| --- | --- |
| [Bruno Rocha Moura、2026-05-14 投稿](https://www.brunorochamoura.com/posts/oswe-guide/) | Web Security Academy を基礎固めに使い、WEB-300 の脆弱なアプリごとに自分で PoC を書くことを勧める。`argparse` で対象や必要なリスナー情報を受け取り、短い関数で処理を組み立て、繰り返す部分をスニペットとして蓄積するという本人の学習方針。 |
| [b1uef0x、2026-02 合格](https://b1ue.x0.com/article/2026/0226/) | Challenge Labs を Python で自動化し、使った処理を機能別チートシートに整理した。PDF からコピーした Python のインデント崩れを懸念し、base64 と復元手順・ハッシュも記載したという経験。base64 記載は公式ガイドでも許容されるが、必須ではない。 |
| [Tony Harris、2025-10-06 投稿](https://tonyharris.io/posts/oswe_writeup/) | 事前にボイラープレートを用意した一方、リスナー起動、Exploit 発火、シェル受信を 1 本にまとめる部分で時間を使った。コマンドと出力を記録してレポートに備えることを勧める。 |
| [holywater、2026-08-14 投稿](https://holywater.dev/blog/oswe/) | PoC の再利用部分として引数解析、Cookie を保つセッション、コールバック受信、ペイロード配信を挙げ、失敗箇所を追えるスクリプトの重要性を述べる。本人はテンプレートを利用したが、そのテンプレートの使用は試験要件ではない。 |
| [Riyan Firmansyah、2026-08-17 投稿](https://ruz.fi/en/posts/my-experience-taking-the-oswe-certification-from-offsec/) | 初回はスクリプトの小さなミスで得点を失ったと報告。再受験時は変更のたびに対象を初期化して通しで再実行し、変数や一回で動くかを確認した。英語記事は本人が公開した AI 補助翻訳。 |

holywater が利用した [kwkeefer/cookiecutter-poc](https://github.com/kwkeefer/cookiecutter-poc) は、引数付き CLI、HTTP コールバックサーバー、ペイロード配信、シェル受信などを備える**複数ファイルの汎用テンプレート**である。これは本人の採用例であり、OffSec が指定した形式ではない。単純な Web Security Academy Lab には機能を絞った 1 ファイルのほうが攻撃の理解と自力実装に適するというのが、このリポジトリでの判断である。複数段階の PoC でコールバックやシェル受信が必要になったとき、同テンプレートの構成を参考にできる。[受験記](https://holywater.dev/blog/oswe/)・[テンプレートの README](https://github.com/kwkeefer/cookiecutter-poc)

[rizemon/exploit-writing-for-oswe](https://github.com/rizemon/exploit-writing-for-oswe) は、`requests` の使い方、リクエストの調査方法、再利用コードをまとめたコミュニティの参考資料である。著者自身が速度優先で一般的なコーディング慣行に反する例もあると断っており、`assert` による成功判定や開発中の Cookie のハードコードなどは、そのまま共通規約には採用しない。

Bruno のガイドにある `requests.get(..., verify=False)` と警告抑制は、証明書検証を無効にする例であり、このリポジトリの既定値にはしない。必要な環境でのみ、理由を確認して設定する。[Bruno のコード例](https://www.brunorochamoura.com/posts/oswe-guide/)・[Requests の証明書検証](https://requests.readthedocs.io/en/stable/user/advanced/#ssl-cert-verification)

## このリポジトリでの学習への反映（提案）

1. Web Security Academy の**単一脆弱性 Lab は 1 ファイルの短い PoC**として自力で書く。これは練習単位であり、複数の脆弱性を連結する OSWE の提出形式そのものではない。[公式要件](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)
2. 各 PoC で、対象 URL 等の引数、セッション管理、攻撃の各段階、成功を裏付ける出力、失敗理由を明確にする。コールバックが必要な題材ではリスナーのアドレスとポートも引数にする。再利用する断片は、必要性が実際に現れてから整理する。[Bruno の学習方針](https://www.brunorochamoura.com/posts/oswe-guide/)・[holywater の経験](https://holywater.dev/blog/oswe/)・[b1uef0x の経験](https://b1ue.x0.com/article/2026/0226/)
3. 手動で解けた後も、初期状態から無対話で再実行できるかを検証する。後に複数段階の Lab で、認証・Cookie・コールバック・検証を一連の流れに組み込む。[Riyan の経験](https://ruz.fi/en/posts/my-experience-taking-the-oswe-certification-from-offsec/)・[公式要件](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)
4. 現在の反射型 XSS Lab で `requests` による反射確認までを行う場合は、その結果を **HTML 応答中の反射の証拠**として表現する。JavaScript の実行や Lab の解決を確認したとは書かない。これは本 Lab の検証範囲を正確に示すための整理である。

試験を受ける直前には、上記リンクの OffSec ガイドと FAQ を再確認する。受験記に記載された対象の台数・内訳や本人固有の実装選択は、当日の指示より優先しない。[公式ガイド](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)
