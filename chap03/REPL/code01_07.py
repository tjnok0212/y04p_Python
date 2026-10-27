# -*- coding: utf-8 -*-

def main():
    # 集合型を生成
    colors = {
        "red",
        "green",
        "blue",
        }
    print("Done: colors = {\"red\", \"green\", \"blue\",}")

    # 空っぽの集合型を生成
    e = set(); print("Done: e = set()")
    print("e:", e)

    # set() を使って集合型を生成
    fruits = set([
        "orange",
        "banana",
        "mango",
        ])
    print("Done: fruits = set({\"orange\", \"banana\", \"mango\",})")
    print("fruits:", fruits)
    fruits = {
        "orange",
        "banana",
        "mango",
        "banana",
        "mango",
        }
    print("Done: fruits = {\"orange\", \"banana\", \"mango\", \"banana\", \"mango\",}")
    print("fruits:", fruits)
    return


if __name__ == "__main__":
    main()