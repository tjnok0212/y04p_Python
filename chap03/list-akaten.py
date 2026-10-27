# -*- coding: utf-8 -*-

def main():
    # 国語の点数一覧
    points = [
        80,
        40,
        23,
        14,
        29,
        58,
        ]

    # 30点未満のデータだけを選んで赤点リストに追加
    akaten = []
    for p in points:
        if p < 30:
            akaten.append(p)

    # 選んだデータを表示
    print("akaten :", akaten)
    return


if __name__ == "__main__":
    main()