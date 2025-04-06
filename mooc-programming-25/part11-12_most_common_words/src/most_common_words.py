import re
def most_common_words(filename: str, lower_limit: int):
    file = open(filename) 
    document_text = file.read()
    document_without = re.sub(r'[^\w\s]', '', document_text)
    document_new = document_without.split()
    return {word: document_new.count(word) for word in document_new if document_new.count(word) >= lower_limit}

if __name__ == "__main__":
    common_word = most_common_words("comprehensions.txt", 3)
    print(common_word)