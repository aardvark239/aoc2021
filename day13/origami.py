import numpy as np


def main():
    with open("input.txt") as f:
        flag = True
        l = []
        fold = []
        n = m = 0
        for line in f:
            if line == "\n":
                flag = False
                continue
            if flag:
                tmp = [int(x) for x in line.strip().split(",")]
                l += [(tmp[0], tmp[1])]
                if n < tmp[0]:
                    n = tmp[0]
                if m < tmp[1]:
                    m = tmp[1]
            else:
                tmp = line.strip().split("=")
                fold += [(tmp[0][-1], int(tmp[1]))]

    l_new = l[:]
    for fld in fold:
        if fld[0] == "x":
            for i, el in enumerate(l_new):
                l_new[i] = (el[0] if el[0] < fld[1] else 2*fld[1] - el[0], el[1])
                n = fld[1] - 1
        else:
            for i, el in enumerate(l_new):
                l_new[i] = (el[0], el[1] if el[1] < fld[1] else 2*fld[1] - el[1])
                m = fld[1] - 1
    M = np.zeros((n+1, m+1))
    for p in l_new:
        M[p[0]][p[1]] = 1
    M = M.transpose()
    print((M == 1).sum())


if __name__ == "__main__":
    main()