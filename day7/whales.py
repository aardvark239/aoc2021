def min_fuel(pos):
    m = min(pos)
    M = max(pos)
    d = {}
    for n in pos:
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1
    s = sum(pos) - m * len(pos)
    res = s
    c = d[m]
    N = len(pos)
    for i in range(m+1, M+1):
        s += 2 * c - N
        if res > s:
            res = s
        if i in d.keys():
            c += d[i]
    return res


def min_fuel_exp(pos):
    m = min(pos)
    M = max(pos)
    d = {}
    for n in pos:
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1
    tot_r = res = sum([(x-m)*(x-m+1)//2 for x in pos])
    tot_l = 0
    s_l = m * d[m]
    s_r = sum(pos) - m*d[m]
    n_l = d[m]
    n_r = len(pos) - d[m]
    for i in range(m+1, M+1):
        tot_l += n_l * i - s_l
        tot_r -= s_r - n_r * (i-1)
        #print(tot_l+tot_r)
        if res > tot_l + tot_r:
            res = tot_l + tot_r
        if i in d.keys():
            n_l += d[i]
            n_r -= d[i]
            s_l += d[i] * i
            s_r -= d[i] * i
    return res


def main():
    with open("input.txt") as f:
        pos = [int(x) for x in f.readline().strip().split(",")]
    print(min_fuel_exp(pos))


if __name__ == "__main__":
    main()