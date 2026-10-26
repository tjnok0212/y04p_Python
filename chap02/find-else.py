# -*- coding: utf-8 -*-

def main():
    # for 構文で else を記述する場合
    # 食材一覧
    food_list = [
        "Banana",
        "Mango",
        "Fish",
        "Carrot",
        "Cabbage",
        ]

    # マンゴーがないか確認する
    for food in food_list:
        if food == "Mango":
            print("マンゴーが入っています")
            break
    else:
        print("ありません")
    return


if __name__ == "__main__":
    main()
