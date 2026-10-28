# -*- coding: utf-8 -*-

from common.exec_logger import run_and_done, show_env

def main():
    # リストの生成
    # a = [
    #     10,
    #     22,
    #     30,
    #     45,
    #     ]
    env = {}
    run_and_done("a = [10, 22, 30, 45,]", env)
    run_and_done("a[1] = 555", env)
    print(f"Done: a = {env["a"]}")

    print("-"*30)
    run_and_done("a = [i for i in range(1, 8)]", env)
    # a = list(range(1,8)) でも可
    print(f"Done: len(a) = {len(env["a"])}")

    run_and_done("b = [i*2 for i in range(4)]", env)
    print(f"Done: len(b) = {len(env["b"])}")
    return


if __name__ == "__main__":
    main()