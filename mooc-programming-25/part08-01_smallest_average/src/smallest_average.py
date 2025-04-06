def smallest_average(person1: dict, person2: dict, person3: dict):
    num1 = []
    num2 = []
    num3 = []
    for value in person1:
        num1.append(person1[value])
    del num1[0]
    sum1 = sum(num1)

    for value in person2:
        num2.append(person2[value])
    del num2[0]
    sum2 = sum(num2)
    
    for value in person3:
        num3.append(person3[value])
    del num3[0]
    sum3 = sum(num3)
    
    sums = [sum1, sum2, sum3]
    if sum1 == min(sums):
        return person1
    elif sum2 == min(sums):
        return person2
    else:
        return person3

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))