# -*- coding: utf-8 -*-

import textwrap
from common.exec_logger import run_and_done


def main():
    env = {}
    run_and_done(textwrap.dedent("""
        team1 = {
            "遠藤",
            "佐藤",
            "中村",
            }\
        """), env)
    run_and_done(textwrap.dedent("""
        team2 = {
            "田中",
            "遠藤",
            "中村",
            }\
        """), env)
    run_and_done("team3 = team1 | team2", env)
    print(f"team3 = {env["team3"]}")
    run_and_done("team4 = team1 & team2", env)
    print(f"team4 = {env["team4"]}")
    run_and_done("team5 = team1 ^ team2", env)
    print(f"team5 = {env["team5"]}")
    return


if __name__ == "__main__":
    main()