# -*- coding: UTF-8 -*-

class Main():
    __PER_INCH = 2.54

    def __init__(
            self,
            inch = 1,
            ):
        self.__inch = inch
        self.__calc()
        return

    def __calc(self):
        self.__cm = self.__inch * self.__PER_INCH
        return self

    def view1(self):
        desc = str(self.__inch) + "インチ = " + str(self.__cm) + "センチ"
        print(desc)
        return self

    def view2(self):
        desc = "{0:.2f}インチ = {1:.2f}センチ".format(self.__inch, self.__cm)
        print(desc)
        return self

    def view3(self):
        desc = f"{self.__inch:.2f}インチ = {self.__cm:.2f}センチ"
        print(desc)
        return self


if __name__ == "__main__":
    Main(float(input("何インチですか？> "))).view3()