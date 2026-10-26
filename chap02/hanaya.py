# -*- coding: utf-8 -*-

class Hanaya():
    __PRICE_ROSE = 500
    __PRICE_SUN_FLOWER = 400
    __PRICE_TULIP = 700

    def __init__(
            self,
            num_rose = 0,
            num_sun_flower = 0,
            num_tulip = 0,
            ):
        self.__num_rose = num_rose
        self.__num_sun_flower = num_sun_flower
        self.__num_tulip = num_tulip

        return

    def add_num_rose(
            self,
            num,
            ):
        self.__num_rose += num
        return self

    def add_num_sun_flower(
            self,
            num,
            ):
        self.__num_sun_flower += num
        return self

    def add_num_tulip(
            self,
            num,
            ):
        self.__num_tulip += num
        return self

    def buy_rose(self):
        return self.__PRICE_ROSE * self.__num_rose

    def buy_sun_flower(self):
        return self.__PRICE_SUN_FLOWER * self.__num_sun_flower

    def buy_tulip(self):
        return self.__PRICE_TULIP * self.__num_tulip

    def calc_flower(self):
        return self.buy_rose() + self.buy_sun_flower() + self.buy_tulip()


if __name__ == "__main__":
    hanaya = Hanaya(
        num_rose = 18,
        num_sun_flower = 8,
        num_tulip = 21,
        )
    hanaya.add_num_sun_flower(-2).add_num_tulip(-5)
    sum_price = hanaya.calc_flower()
    print("買い物の合計は、{:.0f}円".format(sum_price))
    print("割引してもらうと、{:.0f}円".format(sum_price * 0.9))