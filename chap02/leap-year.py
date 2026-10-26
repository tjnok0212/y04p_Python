# -*- coding: utf-8 -*-

class main():
    __is_leap = False
    __is_judge = True
    def __init__(
            self,
            year = -1,
            ):
        self.__input_y = year if year > 0 else int(input("西暦何年？> "))
        self.__value_check()
        self.__judge_leap03()
        return

    def __judge_leap01(self):
        if self.__input_y % 4 == 0:
            if self.__input_y % 100 == 0:
                if self.__input_y % 400 == 0:
                    self.__is_leap = True
                else:
                    pass
            else:
                self.__is_leap = True
        else:
            pass
        return self

    def __judge_leap02(self):
        if self.__input_y % 400 == 0:
            self.__is_leap = True
        elif self.__input_y % 100 == 0:
            pass
        elif self.__input_y % 4 == 0:
            self.__is_leap = True
        else:
            pass
        return

    def __judge_leap03(self):
        self.__is_leap = (self.__input_y % 400 == 0) or ((self.__input_y % 100 != 0) and (self.__input_y % 4 == 0))
        return self

    def view_result(self):
        if self.__is_judge:
            print("{input}年は".format(input=self.__input_y), end="")
            if self.__is_leap:
                print("うるう年です")
            else:
                print("平年です")
        else:
            print("不正な入力値です")
        return

    def __value_check(self):
        if self.__input_y < 0:
            self.__is_judge = False
        return self


if __name__ == "__main__":
    main().view_result()
