# -*- coding: utf-8 -*-

class FruitsShop():
    def __init__(self):
        self.fruits = {
            "Banana": 300,
            "Orange": 240,
            "Strawberry": 350,
            "Mango": 400,
            }
        return

    def view1(self):
        # 辞書型のデータ一覧を表示
        for name in self.fruits.keys():
            # 値段情報を取得
            price = self.fruits[name]

            # 画面出力
            s = f"{name} is {price} yen"
            print(s)
            continue
        return self

    def view2(self):
                # 辞書型のデータ一覧を表示
        for name, price in self.fruits.items():
            # 画面出力
            s = f"{name} is {price} yen"
            print(s)
            continue
        return self


if __name__ == "__main__":
    FruitsShop().view2()