# -*- coding: UTF-8 -*-

class calcDaikei():
    def __init__(self, upper_base=2, lower_base=3, height=4):
        self.__upper_base = upper_base
        self.__lower_base = lower_base
        self.__height = height
        return

    def set_upper_base(self, upper_base) :
        self.__upper_base = upper_base
        return self

    def set_lower_base(self, lower_base):
        self.__lower_base = lower_base
        return self

    def set_height(self, height):
        self.__height = height
        return self

    def calc_menseki(self):
        menseki = (self.__upper_base + self.__lower_base) * self.__height / 2
        print("台形の面積は", menseki, "cm2", sep="")
        return menseki

if __name__ == "__main__":
    daikei = calcDaikei()
    daikei.calc_menseki()
