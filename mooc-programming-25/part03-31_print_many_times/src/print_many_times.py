def print_many_times(text, times):
    num = 1
    while num <= times:
        print(f"{text}")
        num += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)