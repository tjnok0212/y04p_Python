# -*- coding: utf-8 -*-

def main():
    a = [10, 555, 30, 45]; print("Done: a = [10, 555, 30, 45]")
    print("a[1:3]:", a[1:3])

    print("-"*30)
    b = list(range(10)); print("Done: b = list(range(10))")
    print("b[1:3]:", b[1:3])
    print("b[:3]:", b[:3])
    print("b[7:]:", b[7:])
    print("b[-1]:", b[-1])
    print("b[-2]:", b[-2])
    print("b[-3:]:", b[-3:])

    print("-"*30)
    b = list(range(10)); print("Done: b = list(range(10))")
    print("b[2:8:2]:", b[2:8:2])
    print("b[::3]:", b[::3])
    print("b[::-1]:", b[::-1])

    print("-"*30)
    nums = list(range(5)); print("Done: nums = list(range(5))")
    del nums[2]; print("Done: del nums[2]")
    print("nums:", nums)
    print()
    nums = list(range(5)); print("Done: nums = list(range(5))")
    del nums[2:4]; print("Done: del nums[2:4]")
    print("nums:", nums)

    print("-"*30)
    a = [1]*3; print("Done: a = [1]*3")
    b = [2]*3; print("Done: b = [2]*3")
    print("a + b:", a + b)
    return


if __name__ == "__main__":
    main()
