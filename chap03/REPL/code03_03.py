# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    run_and_done(textwrap.dedent("""\
        a = [char * 3 for char in ("a", "b", "c")]\
        """), env)
    print(textwrap.dedent(f"""\
        "-".join(a) = {"-".join(env["a"])}\
        """))

    run_and_done(textwrap.dedent("""\
        s = "2020/02/20"\
        """), env)
    run_and_done(textwrap.dedent("""\
        a = s.split("/")\
        """), env)
    print(f"a = {env["a"]}")
    run_and_done(textwrap.dedent("""\
        s = "-".join(a)\
        """), env)
    print(f"s = {env["s"]}")

    run_and_done(textwrap.dedent("""\
        s = "This is a pen."\
        """), env)
    print(textwrap.dedent(f"""\
        s.replace("pen", "note") = {env["s"].replace("pen", "note")}\
        """))
    print(f"s = {env["s"]}")
    return


if __name__ == "__main__":
    main()