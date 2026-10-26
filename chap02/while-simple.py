# -*- coding: utf-8 -*-

def main(input_i):
    energy = input_i
    while energy > 0:
        print("+ 走る")
        print("| energy =", energy)
        energy -= 1
    else:
        return


if __name__ == "__main__":
    main(int(input("エネルギー量> ")))