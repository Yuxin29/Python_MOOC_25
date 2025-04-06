def first_word(sentence):
    sentence[n1] == " "
    return sentence[0: n1]
    
def second_word(sentence):
    sentence[n1] == " "
    sentence2 = sentence[(n1 + 1): ]
    if sentence2[n2] == " ":
        sentence3 = sentence2[0: (n2 + 1)]
        return sentence3

def last_word(sentence):
    while sentence[n] == " ":
        sentence = sentence[(n + 1): ]
    return sentence

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))