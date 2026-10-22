# -*- coding: UTF-8 -*-

class main():
    def __init__(self):
        self.__kion = 30
        return

    def merge_str_and_int_NG(self):
        # 数値と文字列を結合しようとする（正しく動かない例）
        print("今日の気温は" + self.__kion + "度です。")
        return self

    def merge_str_and_int_OK(self):
        # 数値と文字列を結合しようとする（正しく動く例）
        print("今日の気温は" + str( self.__kion ) + "度です。")
        return self

    