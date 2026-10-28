# -*- coding: utf-8 -*-

def main():
    # 2つの文字列を生成
    s1 = "abc"; print("Done: s1 = \"abc\"")
    print("s1:", s1)
    s2 = "def"; print("Done: s2 = \"def\"")
    print("s2:", s2)

    # 「+」演算子で結合する
    s = s1 + s2; print("Done: s = s1 + s2")
    print("s:", s)

    print("-"*30)
    s = "@"; print("Done: s = \"@\"")
    print("s * 3:", s * 3)
    print("love * 3:", "love" * 3)

    print("-"*30)
    s = "abcd"; print("Done: s = \"abcd\"")
    print("s[0]:", s[0])
    print("s[1]:", s[2])

    print("-"*30)
    s = "abcdefg"; print("Done: s = \"abcdefg\"")
    print("s[1:4]:", s[1:4])
    print("s[2:3]:", s[2:3])

    print("-"*30)
    n = "0123456789"
    print("n[2:5]:", n[2:5])
    print("n[4:9]:", n[4:9])
    print("n[5:8]:", n[5:8])
    print("n[3:3]:", n[3:3])
    print("n[:3]:", n[:3])
    print("n[7:]:", n[7:])
    print("n[-1]:", n[-1])
    print("n[-3:]:", n[-3:])
    print("n[0:9:2]:", n[0:9:2])
    print("n[::3]:", n[::3])
    return


if __name__ == "__main__":
    main()