# -*- coding: utf-8 -*-

class Main():
    def __init__(
            self,
            name="jiro",
            age=19,
            ):
        # 名前と年齢を代入
        self.__name = name
        self.__age = age
        return

    def view(self):
        desc = self.__name + "は今年で" + str(self.__age) + "才です。"
        print(desc)
        return self


if __name__ == "__main__":
    Main().view()
