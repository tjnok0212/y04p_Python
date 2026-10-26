# -*- coding: utf-8 -*-

import textwrap

class Main():
    def __init__(self):
        self.triple_quote1().triple_quote2()
        return

    def triple_quote1(self):
        __str = textwrap.dedent(
                    """\
                    今日はいい天気です。
                    明日もいい天気です。
                    でも明後日は雨です。\
                    """
                    )
        print(__str)
        return self

    def triple_quote2(self):
        __str = textwrap.dedent(
                    """\
                    今日はいい天気です。
                    明日もいい天気です。
                    でも明後日は雨です。\
                    """
                    )
        print(__str)
        return self


if __name__ == "__main__":
    Main()