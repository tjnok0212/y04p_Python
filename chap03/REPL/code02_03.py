# -*- coding: utf-8 -*-

from common.exec_logger import run_and_done

def main():
    env = {}
    run_and_done("a, b, c = [2, 300, 4000]", env)
    print(f"a = {env["a"]}")
    print(f"a, b, c = {env["a"]}, {env["b"]}, {env["c"]}")
    return


if __name__ == "__main__":
    main()
