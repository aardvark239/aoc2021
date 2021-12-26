def count_threes(l):
    c = 0
    for i in range(3, len(l)):
        if l[i] > l[i-3]:
            c += 1
    return(c)

def main():
    l = []
    with open("input.txt") as f:
        for line in f:
          l += [int(line)]
    c = 0
    for i in range(1,len(l)):
        if l[i] > l[i-1]:
            c += 1
    print(c)
    print(count_threes(l))


if __name__ == "__main__":
    main()
