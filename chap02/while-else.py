# -*- coding: utf-8 -*-

def main():
    print("整数を入力してください\n終了する際は 'q' または未入力状態でEnterしてください")
    i = int(input("> "))
    while i < 5:
        if i < 0:
            break
        print("while(in) =", i)
        i += 1
        continue
    else:
        print("while(in) =", i)
    return

if __name__ == "__main__":
    main()