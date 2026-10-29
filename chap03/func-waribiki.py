#-*- coding: utf-8 -*-

# スーパーの割引計算
def calcValue(
        who,
        hour:int,
        count:int,
        value:float,
        ) -> None:
    """
    あるスーパーの割引を計算する関数
    """

    info = "割引なし"

    # 14時に商品を3つ以上で1割引き
    if (hour == 14) and (count >= 3):
        value *= .9
        info = "1割引き"

    elif(hour == 15) and (count >= 5):
        value *= .8
        info = "2割引き"

    # 結果を表示
    value = int(value)
    print(f"{who}さんは{info}={value}円")
    return


if __name__ == "__main__":
    # A/B/Cさん、それぞれの支払金額を求める
    calcValue("Alice", 15, 3, 1200)
    calcValue("Bob", 14, 5, 2000)
    calcValue("Charlie", 15, 8, 5400)