# -*- coding: UTF-8 -*-

class main():
    __per_inch = 2.54

    def __init__(self, inch=1):
        self.__cm = inch * self.__per_inch
        print(inch,  "inch = ", self.__cm, "cm")
        return

if __name__ == "__main__":
    main(8)