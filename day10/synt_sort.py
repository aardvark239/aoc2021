def main():
    expected = {"}": "{", ")": "(", "]": "[", ">": "<"}
    points = {"}": 1197, ")": 3, "]": 57, ">": 25137}
    pc = {"{": 3, "(": 1, "[": 2, "<": 4}
    res = []
    with open("input.txt") as f:
        for line in f:
            agg = []
            tmp = True
            s = line.strip()
            for ch in s:
                if ch in expected.keys():
                    if not agg or expected[ch] != agg.pop():
                        #res += points[ch]
                        tmp = False
                        break
                else:
                    agg.append(ch)
            if tmp:
                c = 0
                while agg:
                    c = 5*c + pc[agg.pop()]
                res += [c]
    res = sorted(res)
    print(res[len(res) // 2])


if __name__ == "__main__":
    main()
