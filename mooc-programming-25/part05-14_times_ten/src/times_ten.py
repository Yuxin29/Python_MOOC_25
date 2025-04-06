def times_ten(start_index: int, end_index: int):
    table = {}
    num0 = start_index
    while num0 <= end_index:
        table[num0] = num0 * 10
        num0 += 1
    return table

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)