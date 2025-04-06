def prime_numbers():
    prime = 2
    yield prime
    prime = 3
    yield prime
    number = 4
    while True:
        judgement = []
        for i in range(2, number-1):
            if number % i != 0:
                judgement.append(True)
            else:
                judgement.append(False)
        if all(judgement) == True:
            yield number
            number += 1 
        else:    
            number += 1 
            
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))