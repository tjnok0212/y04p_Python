# -*- coding: utf-8 -*-

def main():
    a = [char * 3 for char in ("a", "b", "c")]
    print("Done: a = [char * 3 for char in (\"a\", \"b\", \"c\")]")
    print("\"-\".join(a):", "-".join(a))

    print("-"*30)
    s = "2020/02/20"; print("Done: s = \"2020/02/20\"")
    a = s.split("/"); print("Done: a = s.split(\"/\")")
    print("a:", a)
    s = "-".join(a); print("Done: s = \"-\".join(a)")
    print("s:", s)

    print("-"*30)
    s = "This is a pen."; print("Done: s = \"This is a pen\"")
    print("s.replace(\"pen\", \"note\"):", s.replace("pen", "note"))
    print("s:", s)
    return


if __name__ == "__main__":
    main()