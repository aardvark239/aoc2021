import numpy as np

def main():
    with open("input.txt") as f:
        coord = []
        n = m = 0
        for line in f:
            tmp = [x.strip(' ') for x in line.strip().split("->")]
            fr = [int(x) for x in tmp[0].split(",")]
            to = [int(x) for x in tmp[1].split(",")]
            if n < max(fr[0], to[0]):
                n = max(fr[0], to[0])
            if m < max(fr[1], to[1]):
                m = max(fr[1], to[1])
            #if fr[0] == to[0] or fr[1] == to[1]
            coord += [(fr, to)]
    M = np.zeros((n+1, m+1))
    for c in coord:
        if c[0][0] == c[1][0]:
            for j in range(min(c[0][1], c[1][1]), max(c[0][1], c[1][1])+1):
                M[c[0][0]][j] += 1
        elif c[0][1] == c[1][1]:
            for i in range(min(c[0][0], c[1][0]), max(c[0][0], c[1][0])+1):
                M[i][c[0][1]] += 1
        else:
            i = 1 if c[0][0] < c[1][0] else -1
            j = 1 if c[0][1] < c[1][1] else -1
            p = c[0]
            while p[0] != c[1][0]:
                M[p[0]][p[1]] += 1
                p = (p[0] + i, p[1] + j)
            M[p[0]][p[1]] += 1
    print((M > 1).sum())


if __name__ == "__main__":
    main()
