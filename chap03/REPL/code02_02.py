# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    # 価格表のデータを変数 prices に代入
    run_and_done(textwrap.dedent("""
        prices = {
            "Banana": 300,
            "Apple": 200,
            "Mango": 400,
            }\
        """), env)

    # Appleはある？
    print(textwrap.dedent(f"""\
        "Apple" in prices = {"Apple" in env["prices"]}\
        """))

    # Orangeはある？
    print(textwrap.dedent(f"""\
        "Orange" in prices = {"Orange" in env["prices"]}\
        """))

    # キーの一覧を得る
    print(f"prices.keys() = {env["prices"].keys()}")

    # キーの一覧をリストで得る
    run_and_done("fruits = list(prices.keys())", env)
    print(f"fruits = {env["fruits"]}")

    # 整列済みの一覧をリストで得る
    print(f"sorted(prices.keys()) = {sorted(env["prices"].keys())}")
    return


if __name__ == "__main__":
    main()