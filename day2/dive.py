def main():
    d = 0
    fr = 0
    a = 0
    with open("input.txt") as f:
        for line in f:
            tmp = line.split()
            if tmp[0] == "forward":
                fr += int(tmp[1])
                d += a * int(tmp[1])
            elif tmp[0] == "down":
                a += int(tmp[1])
            else:
                a -= int(tmp[1])
    print(d * fr)


if __name__ == "__main__":
    main()
