# -*- coding: utf-8 -*-

def main():
    # リストの生成
    a = [
        10,
        22,
        30,
        45,
        ]
    print("Done: a = [10, 22, 30, 45,]")
    print("a =", a)

    a[1] = 555; print("Done: a[1] = 555")
    print("a =", a)

    a = [i for i in range(1, 8)]; print("Done: a = [i for i in range(1, 8)]")
    # a = list(range(1,8)) でも可
    print("len(a):", len(a))

    b = [i*2 for i in range(4)]; print("Done: b = [i*2 for i in range(4)]")
    print("len(b):", len(b))
    return


if __name__ == "__main__":
    main()