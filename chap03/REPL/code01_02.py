# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done

def main():
    env = {}
    # for 構文で enumerate() を使う
    run_and_done(textwrap.dedent("""
        fruits = [
            "Apple",
            "Orange",
            "Banana",
            ]\
        """), env)
    run_and_done(textwrap.dedent("""
        for i, v in enumerate(fruits):
            print(i, v)\
        """), env)
    return


if __name__ == "__main__":
    main()