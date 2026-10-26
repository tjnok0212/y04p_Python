# -*- coding: utf-8 -*-

class Main():
    def __init__(self):
        self.single_quote().double_quote()
        return

    def single_quote(self):
        print('I can\'t play the guiter.')
        return self

    def double_quote(self):
        print("I like \"Orange\".")
        return self


if __name__ == "__main__":
    Main()