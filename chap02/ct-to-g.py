# -*- coding: UTF-8 -*-

class Main():
    __PER_CT = 0.2

    def __init__(
            self,
            ct,
        ):
        self.__ct = ct
        self.__calc()
        return

    def __calc(self):
        self.__g = self.__ct * self.__PER_CT
        return self

    def view(self):
        desc = f"{self.__ct}カラット = {self.__g}グラム"
        print(desc)
        return self


if __name__ == "__main__":
    Main(float(input("何カラットですか？> "))).view()