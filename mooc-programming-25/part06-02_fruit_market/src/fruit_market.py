def read_fruits():
    with open("src/fruits.csv") as new_file:
        chart = {}
        for line in new_file:
            line = line.replace("\n", "")
            part = line.split(";")
            kind = part[0]
            price = float(part[1])
            chart[kind] = price
        return chart

if __name__ == "__main__":
    print(read_fruits())