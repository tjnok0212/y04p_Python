# -*- coding: utf-8 -*-

# 画面に300本の縦線を引く

# グラフィックライブラリを取り込む
from tkinter import *

def main():
    # 画面の初期化
    w = Canvas(
        Tk(),
        width = 900,
        height = 400,
        )
    w.pack()

    # 線をたくさん引く
    for i in range(100):
        x = i * 9
        w.create_line(
            x,
            0,
            x,
            400,
            width = 2.5,
            fill = "#F00" if i % 3 == 0 else "#00F" if i % 3 == 1 else "#0F0",
            )
    mainloop()


if __name__ == "__main__":
    main()