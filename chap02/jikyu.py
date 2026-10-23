# -*- coding: UTF-8 -*-

import textwrap

class Main():
    def __init__(
            self,
            jikyu,
            jikan,
            ):
        self.__jikyu = jikyu
        self.__jikan = jikan
        self.__calc()
        return 

    def __calc(self):
        self.__kyuryou = self.__jikyu * self.__jikan
        return self

    def view(self):
        desc = textwrap.dedent(
                    """\
                    時給{0}円で、{1}時間働いたので...
                    給料は、{2} 円です。\
                    """
                    ).format(self.__jikyu, self.__jikan, self.__kyuryou)
        print(desc)
        return self


if __name__ == "__main__":
    user1 = input("時給はいくらですか？> ")
    user2 = input("何時間働きましたか？> ")
    Main(
        jikyu = int(user1),
        jikan = int(user2),
    ).view()

