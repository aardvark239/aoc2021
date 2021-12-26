def main():
    with open("input.txt") as f:
        line = f.readline().strip().split(",")
        x = [int(p) for p in line[0].split("=")[1].split("..")]
        y = [int(p) for p in line[1].split("=")[1].split("..")]

    print("done")



if __name__ == "__main__":
    main()
