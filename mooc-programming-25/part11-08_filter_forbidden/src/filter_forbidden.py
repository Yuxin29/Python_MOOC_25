import re
def filter_forbidden(string: str, forbidden: str):
    return " ".join([re.sub(f"[{forbidden}]","",word) for word in string.split()])

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)