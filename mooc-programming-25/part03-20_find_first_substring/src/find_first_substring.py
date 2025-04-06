word = input("Please type in a word: ")
cha = input("Please type in a character: ") 
index = word.find(cha)
num = len(word)
if index >= 0 and index + 2 < num:
    print(f"{word[index:(index+3)]}")
else:
    print()