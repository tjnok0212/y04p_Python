# -*- coding: utf-8 -*-

def main():
    while True:
        user = input("坪数は？> ")
        if user == "" or user == "q":
            print("ループを終了します")
            break
        elif not is_num(user):
            print("自然数を入力してください")
            continue

        tubo = float(user)
        if tubo <= 0:
            print("自然数を入力してください")
            continue
        m2 = float(tubo) * 3.31
        s = "{tubo}坪は {m2}平方メートルです".format(tubo = tubo, m2 = m2)
        print(s)
    return 


def is_num(s):
    __judge = True
    try:
        float(s)
    except ValueError:
        __judge = False
    else:
        return __judge


if __name__ == "__main__":
    main()