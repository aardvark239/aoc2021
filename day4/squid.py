
def main():
    with open("input.txt") as f:
        nums = [int(x) for x in f.readline().strip().split(",")]
        l = []
        ll = []
        tmp = []
        for line in f:
            line = line.strip()
            if not line:
                tmp = list(map(list, zip(*tmp)))
                ll += tmp[:]
                tmp = []
                continue
            l += [[int(x) for x in line.split()]]
            tmp += [[int(x) for x in line.split()]]
    ll += tmp[:]
    rows = [len(x) for x in l]
    cols = [len(x) for x in ll]
    s = [sum(x) for x in l]
    ss = [sum(x) for x in ll]
    finished = [1] * (len(s) // 5)
    to_run = len(s) // 5
    ind = 0
    i = 0
    while to_run:
        for k, flag in enumerate(finished):
            tmp = False
            if flag:
                for j in range(5*k, 5*(k+1)):
                    if nums[i] in l[j]:
                        rows[j] -= 1
                        s[j] -= nums[i]
                        if not rows[j] and finished[k]:
                            finished[k] = 0
                            ind = k
                            tmp = True
                    if nums[i] in ll[j]:
                        cols[j] -= 1
                        ss[j] -= nums[i]
                        if not cols[j] and finished[k]:
                            finished[k] = 0
                            ind = k
                            tmp = True
            if tmp:
                print(i)
                print(to_run, nums[i], k)
                to_run -= 1
        i += 1
    res = sum(s[5*ind:5*(ind+1)]) * nums[i-1]

    print(res)


if __name__ == "__main__":
    main()
