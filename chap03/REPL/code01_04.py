# -*- coding: utf-8 -*-

def main():
    # 2つのリストを生成
    n1 = [1, 3, 5]
    n2 = [2, 4, 6]

    # 2つのリストを結合して n3 に代入
    n3 = n1 + n2

    # 内容を確認する
    print("n1 =", n1)
    print("n2 =", n2)
    print("n3 =", n3)

    print("-"*30)

    a = [1, 2, 3]   # リストを生成
    a += [4, 5, 6]  # 異なるリストを追加
    print("a =", a)

    print("-"*30)

    b = [11, 22]        # リストを生成
    b.extend([33, 44])  # 異なるリストを追加
    print("b =", b)
    return


if __name__ == "__main__":
    main()
