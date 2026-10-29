# -*- coding: utf-8 -*-

from common.exec_logger import run_and_done

def main():
    env = {}
    # 2つのリストを生成
    run_and_done("n1 = [1, 3, 5]", env)
    run_and_done("n2 = [2, 4, 6]", env)

    # 2つのリストを結合して n3 に代入
    run_and_done("n3 = n1 + n2", env)

    # 内容を確認する
    print(f"n1 = {env["n1"]}")
    print(f"n2 = {env["n2"]}")
    print(f"n3 = {env["n3"]}")

    run_and_done("a = [1, 2, 3]", env)  # リストを生成
    run_and_done("a += [4, 5, 6]", env) # 異なるリストを追加
    print(f"a = {env["a"]}")

    run_and_done("b = [11, 22]", env)   # リストを生成
    run_and_done("b.extend([33, 44])", env) # 異なるリストを追加
    print(f"b = {env["b"]}")
    return


if __name__ == "__main__":
    main()
