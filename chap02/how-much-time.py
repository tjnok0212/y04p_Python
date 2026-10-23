# -*- coding: UTF-8 -*-

class main():
    def __init__(
            self,
            kyori = 507.5,
            jisoku = 80,
            ):
        self.__kyori = kyori
        self.__jisoku = jisoku
        self.__jikan = self.__kyori / self.__jisoku
        return

    def view(self):
        print(self.__jikan, "時間")
        return self


if __name__ == "__main__":
    main()
