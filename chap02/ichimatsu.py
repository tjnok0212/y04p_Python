# -*- coding: utf-8 -*-

def main(num = 10):
    for i in range(num):
        for j in range(num):
            if (i + j) % 2 == 0:
                print("|",end="")
            else:
                print("-", end="")
        print()
    return


if __name__ == "__main__":
    main()