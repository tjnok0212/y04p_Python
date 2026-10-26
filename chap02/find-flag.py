# -*- coding: utf-8 -*-

def main():
    # for 構文をフラグで分岐する場合
    # 食材一覧
    food_list = [
        "Banana",
        "Mango",
        "Fish",
        "Carrot",
        "Cabbage",
        ]

    # マンゴーがないか確認する
    flag_found = False
    for food in food_list:
        if food == "Mango":
            flag_found = True
            break
    
    if flag_found:
        print("マンゴーが入ってます")
    else:
        print("ありません")
    return


if __name__ == "__main__":
    main()
