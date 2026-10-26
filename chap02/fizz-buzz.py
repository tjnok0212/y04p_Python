# -*- coding: utf-8 -*-

def main():
    # FizzBuzz
    for i in range(1, 21):
        if i % 15 == 0:
            print("Fizz Buzz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        print(i)
        continue
    return

if __name__ == "__main__":
    main()