def longest(strings):
    index = 0
    list_leng = []
    for i in strings:
        lenth = len(i)
        list_leng.append(lenth)
        index += 1 
    max_value = max(list_leng)
    index_max = list_leng.index(max_value)
    return strings[index_max]

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))