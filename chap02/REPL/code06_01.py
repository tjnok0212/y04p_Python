# -*- coding: utf-8 -*-

def main():
    print("---------")
    print(type(30))
    print(type(5.2))
    print(type("abc"))

    print("---------")
    v = 30
    print("v =", v)
    print("v.__add__(5) =", v.__add__(5))
    print("v.bit_length():", v.bit_length())

    print("---------")
    print(dir(30))
    print(dir("abc"))
    return


if __name__ == "__main__":
    main()