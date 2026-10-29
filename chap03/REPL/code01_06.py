# -*- coding: utf-8 -*-

from common.exec_logger import run_and_done

def main():
    env = {}
    # タプル a を作成
    run_and_done("a = (10, 20, 30)", env)
    # その要素を参照する
    print(f"a[1] = {env["a"][1]}")
    # スライス
    print(f"a[:2] = {env["a"][:2]}")
    return


if __name__ == "__main__":
    main()