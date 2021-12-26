import numpy as np
from collections import deque
import copy

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def neighbours(p, n, m):
    for x in moves:
        if 0 <= p[0] + x[0] < n and 0 <= p[1] + x[1] < m:
            yield p[0] + x[0], p[1] + x[1]


def one_step(mat):
    res = mat + 1
    n, m = res.shape
    to_flash = np.argwhere(res > 9)
    c = 0
    q = deque()
    for el in to_flash:
        res[el[0]][el[1]] = 0
        q.append(el)
    while q:
        c += 1
        p = q.popleft()
        for nb in neighbours(p, n, m):
            if res[nb[0], nb[1]]:
                res[nb[0], nb[1]] += 1
                if res[nb[0], nb[1]] > 9:
                    res[nb[0], nb[1]] = 0
                    q.append(nb)
    return res, c


def n_steps(mat, N):
    res = copy.deepcopy(mat)
    c = 0
    for _ in range(N):
        res, n = one_step(res)
        c += n
    return c


def sim_flash(mat):
    res = copy.deepcopy(mat)
    c = 0
    while c < 1000:
        c += 1
        res, tmp = one_step(res)
        if tmp == res.shape[0] * res.shape[1]:
            return c
    return "Tough"


def main():
    mat = []
    with open("input.txt") as f:
        for line in f:
            mat += [[int(x) for x in line.strip()]]
    print(sim_flash(np.array(mat)))


if __name__ == "__main__":
    main()
