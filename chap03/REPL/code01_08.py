# -*- coding: utf-8 -*-

def main():
    box1 = {
        'ハンマー',
        '釘',
        'ペンチ',
        }
    print("Done: box1 = {\'ハンマー\', \'釘\', \'ペンチ\',}")
    box2 = {
        '釘',
        'ペンチ',
        'レンチ',
        }
    print("Done: box2 = {\'釘\', \'ペンチ\', \'レンチ\',}")
    print("box1 - box2:", box1 - box2)

    print("-"*30)
    box3 = {
        'ハンマー',
        '釘',
        'ペンチ',
        }
    print("Done: box3 = {\'ハンマー\', \'釘\', \'ペンチ\',}")
    print("\'ペンチ\' in box3", 'ペンチ' in box3)

    print("-"*30)
    print("box1 | box2:", box1 | box2)
    print("box1 & box2:", box1 & box2)
    return


if __name__ == "__main__":
    main()