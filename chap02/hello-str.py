# -*- coding: UTF-8 -*-

class Main():
    def __init__(self):
        self.double_quote().single_quote()
        return

    def double_quote(self):
        print("Hello, Python")
        return self

    def single_quote(self):
        print('Hello, Python')
        return self


if __name__ == "__main__":
    Main()