# -*- coding:utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    # 辞書型のデータを作成
    run_and_done(textwrap.dedent("""
        ages = {
            "鈴木": 30,
            "井上": 20,
            "伊藤": 22,
            }\
        """), env)
    print(f"ages = {env["ages"]}")

    print(f"ages[\"伊藤\"] = {env["ages"]["伊藤"]}  # 伊藤さんの年齢を確認")
    run_and_done("""ages["鈴木"] = 29   # 鈴木さんの年齢を更新""", env)
    print(f"ages = {env["ages"]}")
    return


if __name__ == "__main__":
    main()