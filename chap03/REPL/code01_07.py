# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    # 集合型を生成
    run_and_done(textwrap.dedent("""\
        colors = {
            "red",
            "green",
            "blue",
            }\
        """), env)

    # 空っぽの集合型を生成
    run_and_done("e = set()", env)
    print(f"e = {env["e"]}")

    # set() を使って集合型を生成
    run_and_done(textwrap.dedent("""
        fruits = set([
            "orange",
            "banana",
            "mango",
            ])\
        """), env)
    print(f"fruits = {env["fruits"]}")
    run_and_done(textwrap.dedent("""
        fruits = {
            "orange",
            "banana",
            "mango",
            "banana",
            "mango",
            }\
        """), env)
    print(f"fruits = {env["fruits"]}")
    return


if __name__ == "__main__":
    main()