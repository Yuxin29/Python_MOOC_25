from random import sample, randint
def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, (upper + 1)))
    weekly_draw = sample(number_pool, amount)
    weekly_draw = sorted(weekly_draw)
    return weekly_draw

if __name__ == "__name__":
    for number in lottery_numbers(7, 1, 40):
        print(number)