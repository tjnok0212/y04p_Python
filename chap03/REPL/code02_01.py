# -*- coding:utf-8 -*-

def main():
    # 辞書型のデータを作成
    ages = {
        "鈴木": 30,
        "井上": 20,
        "伊藤": 22,
        }
    print("Done: ages = {\"鈴木\": 30, \"井上\": 20, \"伊藤\": 22,}")
    print("ages:", ages)

    print("\n--- 伊藤さんの年齢を確認 ---")
    print("ages[\"伊藤\"]:", ages["伊藤"])
    print("\n--- 鈴木さんの年齢を更新 ---")
    ages["鈴木"] = 29; print("Done: ages[\"鈴木\"] = 29")
    print("ages:", ages)
    return


if __name__ == "__main__":
    main()