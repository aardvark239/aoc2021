import numpy as np
import sys

nbs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
nbs_1 = [(0, 1), (1, 0)]


def enlarge(data):
    return np.vstack([
        np.hstack([
            np.where((data + i + j) > 9, (data + i + j) - 9, data + i + j) for i in range(5)
        ]) for j in range(5)
    ])


def neighbours(p, n, m):
    for x in nbs:
        if 0 <= p[0] + x[0] < n and 0 <= p[1] + x[1] < m:
            yield p[0] + x[0], p[1] + x[1]


def dijkstra(M, src):
    n, m = M.shape
    V = [(i, j) for i in range(n) for j in range(m)]
    dist = {v: sys.maxsize for v in V}
    dist[src] = 0
    spt_set = {v: False for v in V}
    to_check = set(neighbours(src, n, m))
    to_check.add(src)
    for cout in V:
        m = sys.maxsize
        min_index = cout
        for v in to_check:
            if dist[v] < m and not spt_set[v]:
                m = dist[v]
                min_index = v

        u = min_index
        spt_set[u] = True
        to_check.remove(u)

        for v in neighbours(u, n, m):
            if not spt_set[v] and dist[v] > dist[u] + M[v[0]][v[1]]:
                dist[v] = dist[u] + M[v[0]][v[1]]
                to_check.add(v)

    return dist[(n-1, m-1)]


def main():
    with open("input.txt") as f:
        l = []
        for line in f:
            l.append([int(x) for x in line.strip()])
    l = enlarge(np.array(l))
    print(dijkstra(l, (0,0)))


if __name__ == "__main__":
    main()
