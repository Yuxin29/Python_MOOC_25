def anagrams(word1, word2):
    list1 = []
    list2 = []
    for character in word1:
        list1.append(character)
    list1.sort()
    for character in word2:
        list2.append(character)
    list2.sort()
    return list1 == list2
    
if __name__ == "__main__":
    print(anagrams("house", "house"))
