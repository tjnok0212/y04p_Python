# -*- coding: utf-8 -*-

def main():
    # for 構文で enumerate() を使う
    fruits = [
        "Apple",
        "Orange",
        "Banana",
        ]

    for i, v in enumerate(fruits):
        print(i, v)
        continue
    return


if __name__ == "__main__":
    main()