# -*- coding: utf-8 -*-

class Main():
    def __init__(self):
        self.merge_str1().merge_str2()
        return

    def merge_str1(self):
        s = "Hello," + "World!"
        print(s)
        return self

    def merge_str2(self):
        __s1 = "Hello,"
        __s2 = "World!"
        __s3 = __s1 + __s2
        print(__s3)
        return self


if __name__ == "__main__":
    Main()
