# -*- coding: utf-8 -*-

from common.exec_logger import run_and_done

def main():
    env = {}
    # リストを生成
    run_and_done("nums = list(range(1, 4))", env)
    print(f"nums = {env["nums"]}")

    # append で値を追加
    run_and_done("nums.append(4)", env)
    run_and_done("nums.append(5)", env)

    # 結果を確認
    print(f"nums = {env["nums"]}")
    return


if __name__ == "__main__":
    main()