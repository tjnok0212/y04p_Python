# -*- coding: utf-8 -*-

def main():
    for i in range(5):
        print("i=", i)
        if i >= 3: continue
        print("- hello!")
    return


if __name__ == "__main__":
    main()