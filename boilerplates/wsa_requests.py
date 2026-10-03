#!/usr/bin/env python3

# Lab: <Lab 名>
# 目的: <確認したい結果>
# 攻撃手順:
# 1. <自分で確認した手順>
# 前提条件: <必要な準備、なければ「なし」>
# 実行: python3 <このファイル名>.py https://TARGET/
# 成功の証拠: <レスポンスや状態の具体的な確認項目>

import argparse
import sys

import requests


class PoCError(Exception):
    """攻撃の目的を確認できなかった場合に使う。"""


def parse_args():
    parser = argparse.ArgumentParser(description="Web Security Academy PoC")
    parser.add_argument("target", help="Lab のベース URL")
    parser.add_argument("--timeout", type=float, default=10, help="リクエストごとの秒数")
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout は 0 より大きい値にしてください")
    return args


def run(session, args):
    """Lab 固有の通信と成功判定を書き、確認できた証拠を返す。"""
    # TODO: args.target、args.timeout、session を使って自分で実装する。
    # 目的を確認できなければ PoCError を送出する。
    raise NotImplementedError("Lab 固有の手順を実装してください")


def main():
    args = parse_args()
    try:
        with requests.Session() as session:
            evidence = run(session, args)
        if not evidence:
            raise PoCError("成功の証拠が得られませんでした")
    except (PoCError, requests.RequestException) as exc:
        print(f"[-] {exc}", file=sys.stderr)
        return 1

    print(f"[+] {evidence}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
