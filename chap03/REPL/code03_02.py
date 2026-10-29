# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    run_and_done(textwrap.dedent("""\
        s = "This is a pen"\
        """), env)
    print(f"s.split() = {env["s"].split()}")

    run_and_done(textwrap.dedent("""\
        s = "2020/02/20"\
        """), env)
    print(textwrap.dedent(f"""\
        s.split("/") = {env["s"].split("/")}\
        """))
    print(textwrap.dedent(f"""\
        s.split("/") = {env["s"].split("/", maxsplit=1)}\
        """))
    return


if __name__ == "__main__":
    main()