# -*- coding: utf-8 -*-

def main():
    team1 = {
        "遠藤",
        "佐藤",
        "中村",
        }
    print("Done: team1 = {\"遠藤\", \"佐藤\", \"中村\",}")
    team2 = {
        "田中",
        "遠藤",
        "中村",
        }
    print("Done: team2 = {\"田中\", \"遠藤\", \"中村\",}")
    team3 = team1 | team2; print("Done: team3 = team1 | team2")
    print("team3:", team3)
    team4 = team1 & team2; print("Done: team4 = team1 & team2")
    print("team4:", team4)
    team5 = team1 ^ team2; print("Done: team5 = team1 ^ team2")
    print("team5:", team5)
    return


if __name__ == "__main__":
    main()