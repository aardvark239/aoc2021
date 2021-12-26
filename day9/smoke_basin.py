import numpy as np
from collections import deque

moves = [(0, 1), (1, 0)]

nbs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def neighbours(p, n, m):
    for x in nbs:
        if 0 <= p[0] + x[0] < n and 0 <= p[1] + x[1] < m:
            yield p[0] + x[0], p[1] + x[1]


def low_points(mat):
    n, m = mat.shape
    checked = np.ones(mat.shape)
    for i in range(n):
        for j in range(m):
            for p in neighbours((i, j), n, m):
                if mat[i][j] < mat[p[0]][p[1]]:
                    checked[p[0]][p[1]] = 0
                elif mat[i][j] > mat[p[0]][p[1]]:
                    checked[i][j] = 0
                else:
                    checked[p[0]][p[1]] = 0
                    checked[i][j] = 0
    res1 = ((mat + 1) * checked).sum()
    res = []
    mask = np.ones(checked.shape)
    for i in range(n):
        for j in range(m):
            if checked[i][j]:
                q = deque()
                q.append((i, j))
                mask[i][j] = 0
                tmp = 0
                while q:
                    p = q.popleft()
                    tmp += 1
                    for nb in neighbours(p, n, m):
                        if mat[p[0]][p[1]] < mat[nb[0]][nb[1]] != 9 and mask[nb[0]][nb[1]]:
                            q.append(nb)
                            mask[nb[0]][nb[1]] = 0
                print(tmp)
                res += [tmp]
    res.sort(reverse=True)
    return np.prod(res[0:3])


def main():
    mat = []
    with open("input.txt") as f:
        for line in f:
            mat += [[int(x) for x in line.strip()]]
    print(low_points(np.array(mat)))


if __name__ == "__main__":
    main()
