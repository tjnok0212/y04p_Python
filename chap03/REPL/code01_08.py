# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    run_and_done(textwrap.dedent("""
        box1 = {
            "ハンマー",
            "釘",
            "ペンチ",
            }
        """), env)
    run_and_done(textwrap.dedent("""
        box2 = {
            "釘",
            "ペンチ",
            "レンチ",
            }
        """), env)
    print(f"box1 - box2 = {env["box1"] - env["box2"]}")

    run_and_done(textwrap.dedent("""
        box3 = {
            "ハンマー",
            "釘",
            "ペンチ",
            }\
        """), env)
    print(textwrap.dedent(f"""\
        "ペンチ" in box3 = {"ペンチ" in env["box3"]}\
        """))

    print(f"box1 | box2 = {env["box1"] | env["box2"]}")
    print(f"box1 & box2 = {env["box1"] & env["box2"]}")
    return


if __name__ == "__main__":
    main()