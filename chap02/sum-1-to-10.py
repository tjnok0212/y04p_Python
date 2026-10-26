# -*- coding: utf-8 -*-

def main():
    v = 0
    for i in range(1, 11):
        v += i
        print(i, "を足すと", v)
    print("1から10を足すと...", v)
    return


if __name__ == "__main__":
    main()