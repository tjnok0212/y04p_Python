# coding: UTF-8 -*-

def Main():
    kion = int(input("本日の気温は？> "))
    if kion >= 25:
        print("氷水を出す")
    else:
        print("熱いお茶を出す")
    return 


if __name__ == "__main__":
    Main()