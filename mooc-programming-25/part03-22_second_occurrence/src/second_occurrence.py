word0 = input("Please type in a string: ")
subword = input("Please type in a substring: ")
index0 = word0.find(subword)
num0 = len(word0)
many = len(subword)
word1 = word0[(index0 + many):num0]
index1 = word1.find(subword)
num1 = len(word1)
if index1 < 0:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index1 + many + index0}.")