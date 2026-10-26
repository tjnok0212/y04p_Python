# -*- coding: utf-8 -*-

import textwrap

class TicketBooth():
    __PRICE_C = 500
    __PRICE_N = 1000
    __PRICE_E = 700

    def __init__(
            self,
            num_c = -1,
            num_n = -1,
            num_e = -1,
            ):
        self.__num_c = num_c if num_c >= 0 else int(input("子供料金(13才未満)は何人？> "))
        self.__num_n = num_n if num_n >= 0 else int(input("通常料金(13-64才)は何人？> "))
        self.__num_e = num_e if num_e >= 0 else int(input("年配者料金(65才以上)は何人？> "))
        self.__calc()
        return

    def __calc(self):
        # 合計人数
        self.__num = self.__num_c + self.__num_n + self.__num_e

        # 各料金ごとの合計金額
        self.__fee_c = self.__num_c * self.__PRICE_C
        self.__fee_n = self.__num_n * self.__PRICE_N
        self.__fee_e = self.__num_e * self.__PRICE_E

        # 合計金額
        self.__fee = self.__fee_c + self.__fee_n + self.__fee_e
        return self

    def view_result(self):
        desc = textwrap.dedent(
                f"""\
                子供料金　：{self.__num_c:2d}人 x {self.__PRICE_C:4d} = {self.__fee_c:5d}円
                通常料金　：{self.__num_n:2d}人 x {self.__PRICE_N:4d} = {self.__fee_n:5d}円
                年配者料金：{self.__num_e:2d}人 x {self.__PRICE_E:4d} = {self.__fee_e:5d}円
                """
                )
        if self.__num >= 10:
            print("団体割引があります")
            self.__fee *= 0.8
        else:
            print("割引はありません")

        desc += f"合計： {self.__num:2d}人 {self.__fee:5.0f}円"
        print(desc)
        return self


if __name__ == "__main__":
    TicketBooth(3, 5, 2).view_result()