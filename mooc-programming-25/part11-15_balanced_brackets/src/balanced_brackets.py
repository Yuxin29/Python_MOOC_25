def balanced_brackets(my_string: str):
    new_string = ''.join(c for c in my_string if c in "[{}()]")
    #return new_string
    while len(new_string) >= 2:
        if new_string[0] == "(" and new_string[-1] == ")" or new_string[0] == "[" and new_string[-1] == "]":
            return balanced_brackets(new_string[1:-1])
            balanced_brackets(new_string)
        else:
            return False
    if len(new_string) == 1:
        return False
    elif len(new_string) == 0:
        return True

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    ok = balanced_brackets("(()]")
    print(ok)

    ok = balanced_brackets("([bad egg)]")
    print(ok)