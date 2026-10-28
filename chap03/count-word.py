# -*- coding: utf-8 -*-

import textwrap

class Main():
    def __init__(self):
        self.text = textwrap.dedent("""
            Keep on asking, and it will be given you;
            keep on seeking, and you will find;
            keep on knocking, and it will be opened to you;
            for everyone asking receives, and everyone seeking finds.
            and to everyone knocking, it will be opened.
            """)
        self.__execute_split()
        self.__execute_count()
        return

    def __execute_split(self):
        # 単語を区切る
        __text = self.text
        for t in (";", ",", "."):
            __text = __text.replace(t, "")
            continue
        self.words = __text.split()
        return self

    def __execute_count(self):
        self.counter = {}
        for w in self.words:
            ws = w.lower()
            if ws in self.counter:
                self.counter[ws] += 1   # 辞書に存在すれば、+1
            else:
                self.counter[ws] = 1    # 辞書に存在しなければ新規追加
        return self

    def view_result(self):
        for k, v in sorted(self.counter.items()):
            if v >= 3:
                print(f"{k}: {v}")
        return self


if __name__ == "__main__":
    Main().view_result()