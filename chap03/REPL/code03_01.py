# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    # 2つの文字列を生成
    run_and_done(textwrap.dedent("""\
        s1 = "abc"\
        """), env)
    print(f"s1 = {env["s1"]}")
    run_and_done(textwrap.dedent("""\
        s2 = "def"\
        """), env)
    print(f"s2 = {env["s2"]}")

    # 「+」演算子で結合する
    run_and_done("s = s1 + s2", env)
    print(f"s = {env["s"]}")

    run_and_done(textwrap.dedent("""\
        s = "@"\
        """), env)
    print(f"s * 3 = {env["s"] * 3}")
    print(f"love * 3 = {"love" * 3}")

    run_and_done(textwrap.dedent("""\
        s = "abcd"\
        """), env)
    print(f"s[0] = {env["s"][0]}")
    print(f"s[2] = {env["s"][2]}")

    run_and_done(textwrap.dedent("""\
        s = "abcdefg"\
        """), env)
    print(f"s[1:4] = {env["s"][1:4]}")
    print(f"s[2:3] = {env["s"][2:3]}")

    run_and_done(textwrap.dedent("""\
        n = "0123456789"\
        """), env)
    print(f"n[2:5] = {env["n"][2:5]}")
    print(f"n[4:9] = {env["n"][4:9]}")
    print(f"n[5:8] = {env["n"][5:8]}")
    print(f"n[3:3] = {env["n"][3:3]}")
    print(f"n[:3] = {env["n"][:3]}")
    print(f"n[7:] = {env["n"][7:]}")
    print(f"n[-1] = {env["n"][-1]}")
    print(f"n[-3:] = {env["n"][-3:]}")
    print(f"n[0:9:2] = {env["n"][0:9:2]}")
    print(f"n[::3] = {env["n"][::3]}")
    return


if __name__ == "__main__":
    main()