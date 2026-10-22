# -*- coding: UTF-8 -*-

class main():
    def __init__(self):
        print("Do calc_ng:", end="")
        self.calc_ng()

        # 改行
        print()

        print("Do calc_ok:", end="")
        self.calc_ok()
        return


    def calc_ng(self):
        30 + 5
        return
    
    def calc_ok(self):
        print(30 + 5)
        return

if __name__ == "__main__":
    main()