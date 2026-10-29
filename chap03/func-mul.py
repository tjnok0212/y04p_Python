# -*- coding: utf-8 -*-

def mul(a:float, b:float) -> float:
    """
    掛け算を行う関数

    引数
    - a: int, float
    - b: int, float

    返値
    - a * b: int, float
    """
    return a * b


if __name__ == "__main__":
    print(mul(2, 3))
    print(mul(10, 3))

    help(mul)