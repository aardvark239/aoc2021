import numpy as np


def main():
    with open("input.txt") as f:
        pos = [int(x) for x in f.readline().strip().split(",")]
    M = 256
    T = np.ones((M+1, 9))
    for i in range(1, M+1):
        T[i][0] = T[i-1][6] + T[i-1][8]
        for j in range(1, 9):
            T[i][j] = T[i-1][j-1]
    print(sum([T[M][x] for x in pos]))


if __name__ == "__main__":
    main()