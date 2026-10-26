# -*- coding: utf-8 -*-

def Main():
    level = int(input("現在のレベルは？> "))
    if level > 5:
        print("レベル5以上の人への補足アドバイス")
    if level > 8:
        print("レベル8以上の人への細くアドバイス")
    return 


if __name__ == "__main__":
    Main()