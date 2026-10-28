# -*- coding: utf-8 -*-

import random as rd

def main():
    kakugen = [
        "能ある鷹は爪を隠す",
        "豚に真珠",
        "二兎を追う者は一兎をも得ず",
        "叩き続けなさい。そうすれば開かれます。",
        ]

    while True:
        user = input("> ")
        if user == "q" or user == "c":
            break
        # ランダムに数値を一つ選ぶ
        ## i = rd.randint(0, len(kakugen)-1)
        i = rd.randrange(len(kakugen))


        # 選んだ格言を表示する
        print(kakugen[i])
    return


if __name__ == "__main__":
    main()