# -*- coding: UTF-8 -*-

class main():
    __PER_INCH = 2.54

    def __init__(
            self,
            inch = 1,
            ):
        self.__cm = inch * self.__PER_INCH
        print(inch,  "inch = ", self.__cm, "cm")
        return


if __name__ == "__main__":
    main(8)