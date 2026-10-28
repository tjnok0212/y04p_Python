# -*- coding: utf-8 -*-

def main():
    # 価格表のデータを変数 prices に代入
    prices = {
        "Banana": 300,
        "Apple": 200,
        "Mango": 400,
        }
    print("Done: prices = {\"Banana\": 300, \"Apple\": 200, \"Mango\": 400,}")

    # Appleはある？
    print("\"Apple\" in prices:", "Apple" in prices)

    # Orangeはある？
    print("\"Orange\" in prices:", "Orange" in prices)

    # キーの一覧を得る
    print("prices.keys():", prices.keys())

    # キーの一覧をリストで得る
    fruits = list(prices.keys()); print("Done: fruits = list(prices.keys());")
    print("fruits:", fruits)

    # 整列済みの一覧をリストで得る
    print("sorted(prices.keys())", sorted(prices.keys()))
    return


if __name__ == "__main__":
    main()