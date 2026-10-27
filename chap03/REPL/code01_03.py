# -*- coding: utf-8 -*-

def main():
    # リストを生成
    nums = list(range(1, 4))
    print("nums =", nums)

    # append で値を追加
    nums.append(4)
    nums.append(5)

    # 結果を確認
    print("nums =", nums)
    return


if __name__ == "__main__":
    main()