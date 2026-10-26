# -*- coding: utf-8 -*-

class Main():
    def __init__(
            self,
            name = "Apple",
            ):
        self.set_name(name)
        return

    def view(
            self,
            num = 3,
            ):
        for i in range(num):
            print(f"{self.__name} {i:04d}")
        return

    def set_name(
            self,
            name,
            ):
        self.__name = name
        return


if __name__ == "__main__":
    Main().view()