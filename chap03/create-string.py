# -*- coding: utf-8 -*-

import textwrap

def main():
    # クォートで文字列を生成する
    s1 = "保つのに時があり捨てるのに時がある"
    s2 = '保つのに時があり捨てるのに時がある'
    print(f"s1: {s1}\ns2: {s2}")

    # 三重引用符(トリプルクォート)で文字列を生成
    s3 = textwrap.dedent("""\
            捜すのに時があり
            あきらめるのに時がある\
            """)
    s4 = textwrap.dedent('''\
            捜すのに時があり
            あきらめるのに時がある\
            ''')
    print(f"s3: {s3}\ns4: {s4}")

    # 数値から返還する
    num = 12345
    s5 = str(num)
    print(f"s5: {s5}")
    return


if __name__ == "__main__":
    main()