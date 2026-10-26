# -*- coding: UTF-8 -*-

def Main():
    print("------------------------------")
    print("3 == 3:", 3 == 3)
    print("3 != 3:", 3 != 3)
    print("100 > 3:", 100 > 3)
    print("5 >= 5:", 5 >= 5)

    print("--- 変数sに文字列を代入 ---")
    s = "pool"
    print("s =", s)
    # 文字列と比較
    print("s == \"bool\":", s == "bool")
    print("s == \"pool\":", s == "pool")

    print("--- 比較式の返却値を確認する ---")
    print("11 == 22:", 11 == 22)
    print("22 == 22:", 22 == 22)
    # 変数aに50を代入
    a = 50
    print("a =", a)
    print("a > 20:", a > 20)

    print("--- and 演算子の例 ---")
    print("True and True:", True and True)
    print("True and False:", True and False)
    # 比較式を用いる場合
    a = 40
    print("a =", a)
    print("(30 <= a) and (a < 50):", (30 <= a) and (a < 50))

    print("--- or 演算子の例 ---")
    print("True or False:", True or False)
    print("False or False:", False or False)
    print("True or True:", True or True)
    print("False or True:", False or True)
    # 比較式を用いる場合
    age = 25
    print("age =", age)
    print("(age < 14) or (age > 70):", (age < 14) or (age > 70)) # 14未満か70超か？
    a = 30
    print("a =", a)
    print("(a % 10 == 0) or (a % 4 == 0):", (a % 10 == 0) or (a % 4 == 0))

    print("--- not 演算子の例 ---")
    print("not True:", not True)
    print("not False:", not False)
    print("not (30 > 5):", not (30 > 5))
    return


if __name__ == "__main__":
    Main()