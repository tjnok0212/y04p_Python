# -*- coding: utf-8 -*-

def main():
    s = "This is a pen"
    print("s.split():", s.split())

    print("-"*30)
    s = "2020/02/20"
    print(s.split("/"))
    print(s.split("/", maxsplit=1))
    return


if __name__ == "__main__":
    main()