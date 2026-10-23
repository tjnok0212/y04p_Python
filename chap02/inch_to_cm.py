# -*- coding: UTF-8 -*-

class main():
    __PER_INCH = 2.54

    def __init__(
            self,
            inch = 1,
            ):
        self.__inch = inch
        self.__cm = inch * self.__PER_INCH
        return

    def view(self):
        desc = str(self.__inch) + "インチ = " + str(self.__cm) + "センチ"
        print(desc)
        return self

    def view2(self):
        desc = "{0:d}インチ = {1:.2f}センチ".format(self.__inch, self.__cm)
        print(desc)
        return self

    def view3(self):
        desc = f"{self.__inch:d}インチ = {self.__cm:.2f}センチ"
        print(desc)
        return self

    def set_inch(
            self,
            inch,
            ):
        self.__inch = inch
        return self


if __name__ == "__main__":
    main(24).view().view2().view3()