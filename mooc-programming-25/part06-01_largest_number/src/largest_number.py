def largest():
    with open("src/numbers.txt") as new_file:
        list = []
        for line in new_file:
            list.append(int(line))
        maxnum = max(list)
        return maxnum

if __name__ == "__main__":
    print(largest())