def main():
    with open("input.txt") as f:
        flag = True
        ins = []
        for line in f:
            if line == "\n":
                flag = False
                continue
            if flag:
                poly = line.strip()
            else:
                tmp = [x.strip(" ") for x in line.strip().split("->")]
                ins += [(tmp[0], tmp[1])]
    d = {}
    for i in range(len(poly) - 1):
        s = poly[i:i+2]
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1
    N = 40
    for _ in range(N):
        d_new = {}
        mask = {x: True for x in d}
        for el in ins:
            if el[0] in d:
                mask[el[0]] = False
                l = el[0][0] + el[1]
                r = el[1] + el[0][1]
                d_new[l] = d_new[l] + d[el[0]] if l in d_new else d[el[0]]
                d_new[r] = d_new[r] + d[el[0]] if r in d_new else d[el[0]]
        for el in mask:
            if mask[el]:
                d_new[el[0]] = d_new[el[0]] + d[el[0]] if el[0] in d_new else d[el[0]]
        d = d_new.copy()
    res = {}
    for el in d:
        res[el[0]] = res[el[0]] + d[el] if el[0] in res else d[el]
        res[el[1]] = res[el[1]] + d[el] if el[1] in res else d[el]
    for x in res:
        res[x] = (res[x] + 1) // 2 if x in [poly[0], poly[-1]] else res[x] // 2
    arr = sorted(list(res.values()))
    print(arr[-1] - arr[0])

if __name__ == "__main__":
    main()
