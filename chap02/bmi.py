# -*- coding: UTF-8 -*-

class MeasureBmi():
    __is_judge = True
    def __init__(
            self,
            weight = -1,
            height = -1,
            ):
        self.__weight = weight if weight > 0 else float(input("体重(kg)は？> "))
        self.__height = height if height > 0 else float(input("身長(cm)は？> "))
        self.__calc_bmi()
        return

    def __calc_bmi(self):
        self.__check_value()
        if self.__is_judge:
            __h = self.__height / 100
            self.__bmi = self.__weight / (__h ** 2)
        else:
            self.__bmi = -1
        return self

    def view_result1(self):
        if self.__is_judge:
            if self.__bmi < 18.5:
                __result = "痩せ型"
            if (18.5 <= self.__bmi) and (self.__bmi < 25):
                __result = "標準体重"
            if (25 <= self.__bmi) and ( self.__bmi < 30):
                __result = "肥満(軽)"
            if self.__bmi >= 30:
                __result = "肥満(重)"
        else:
            __result = "不正入力値"

        print(f"BMI : {self.__bmi:.2f}")
        print(f"判定 : {__result}")
        return self

    def view_result2(self):
        if self.__is_judge:
            if self.__bmi < 18.5:
                __result = "痩せ型"
            if 18.5 <= self.__bmi < 25:
                __result = "標準体重"
            if 25 <= self.__bmi < 30:
                __result = "肥満(軽)"
            if self.__bmi >= 30:
                __result = "肥満(重)"
        else:
            __result = "不正入力値"

        print(f"BMI : {self.__bmi:.2f}")
        print(f"判定 : {__result}")
        return self

    def view_result3(self):
            if self.__is_judge:
                if self.__bmi < 18.5:
                    __result = "痩せ型"
                elif self.__bmi <= 25:
                    __result = "標準体重"
                elif self.__bmi <= 30:
                    __result = "肥満(軽)"
                else:
                    __result = "肥満(重)"
            else:
                __result = "不正入力値"
    
            print(f"BMI : {self.__bmi:.2f}")
            print(f"判定 : {__result}")
            return self

    def __check_value(self):
        if self.__weight <= 0:
            self.__is_judge = False

        if self.__height <= 0:
            self.__is_judge = False

        return self


if __name__ == "__main__":
    MeasureBmi().view_result2()