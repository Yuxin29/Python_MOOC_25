word1 = input("Password: ")
word2 = input("Repeat password: ")
while word2 != word1:
    print("They do not match!")
    word2 = input("Repeat password: ")
print("User account created!") 