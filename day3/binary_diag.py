def bits_to_num(bit_list):
    out = 0
    for bit in bit_list:
        out = (out << 1) | bit
    return out


def main():
    n = 0
    with open("input.txt") as f:
        inp = []
        l = []
        for line in f:
            tmp = [int(x) for x in line.strip()]
            inp += [tmp]
            if not l:
                l = [0] * len(tmp)
            l = [sum(x) for x in zip(l, tmp)]
            n += 1
    gr = [int(x/n > 0.5) for x in l]
    er = [1-x for x in gr]
    res = bits_to_num(gr) * bits_to_num(er)
    print(res)
    ogr = inp[:]
    csr = inp[:]
    i = 0
    while len(ogr) > 1 and i < len(gr):
        tmp = int(sum([x[i] for x in ogr])/len(ogr) >= 0.5)
        ogr = [x for x in ogr if x[i] == tmp]
        i += 1
    i = 0
    while len(csr) > 1 and i < len(er):
        tmp = int(sum([x[i] for x in csr])/len(csr) < 0.5)
        csr = [x for x in csr if x[i] == tmp]
        i += 1
    res = bits_to_num(ogr[0]) * bits_to_num(csr[0])
    print(res)

if __name__ == "__main__":
    main()
