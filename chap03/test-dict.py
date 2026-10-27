# -*- coding: utf-8 -*-

class TestResult():
    def __init__(self):
        self.records = {
            "Tanaka": 72,
            "Yamada": 65,
            "Hirata": 100,
            "Akai": 56,
            "Fukuda": 66,
            "Sakai": 80,
            }
        self.__calc_sum()
        self.__calc_ave()
        return

    def __calc_sum(self):
        self.sum_v = 0
        for v in self.records.values():
            self.sum_v += v
            continue
        return self

    def __calc_ave(self):
        try:
            self.ave_v = self.sum_v / len(self.records)
        except NameError:
            self.__calc_sum()
            self.__calc_ave()
        return self

    def view_general(self):
        print("合計点:", self.sum_v)
        print("平均点:", self.ave_v)
        return self

    def view_detail(self):
        fmt = "| {name:<7} | {v:>4} | {diff_v:>5} |"
        print("| 名前    | 点数 |    差 |")
        for name, v in sorted(self.records.items()):
            # 平均点との差を求める
            diff_v = v - self.ave_v
            # 小数点以下を丸める
            diff_v = round(diff_v, 1)   # diff_v の値を小数点以下1位になるように四捨五入
            # 書式に沿って出力
            print(fmt.format(name=name, v=v, diff_v=diff_v))
            continue
        return self


if __name__ == "__main__":
    TestResult().view_general().view_detail()
