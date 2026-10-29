# -*- coding: utf-8 -*-

from common.exec_logger import run_and_done

def main():
    env = {}
    run_and_done("a = [10, 555, 30, 45]", env)
    print(f"a[1:3] = {env["a"]}")

    print(f"-"*30)
    run_and_done("b = list(range(10))", env)
    print(f"b[1:3] = {env["b"][1:3]}")
    print(f"b[:3] = {env["b"][:3]}")
    print(f"b[7:] = {env["b"][7:]}")
    print(f"b[-1] = {env["b"][-1]}")
    print(f"b[-2] = {env["b"][-2]}")
    print(f"b[-3:] = {env["b"][-3:]}")

    print(f"-"*30)
    run_and_done("b = list(range(10))", env)
    print(f"b[2:8:2] = {env["b"][2:8:2]}")
    print(f"b[::3] = {env["b"][::3]}")
    print(f"b[::-1] = {env["b"][::-1]}")

    print(f"-"*30)
    run_and_done("nums = list(range(5))", env)
    run_and_done("del nums[2]", env)
    print(f"nums = {env["nums"]}")
    print()
    run_and_done("nums = list(range(5))", env)
    run_and_done("del nums[2:4]", env)
    print(f"nums = {env["nums"]}")

    print(f"-"*30)
    run_and_done("a = [1]*3", env)
    run_and_done("b = [2]*3", env)
    print(f"a + b = {env["a"] + env["b"]}")
    return


if __name__ == "__main__":
    main()
