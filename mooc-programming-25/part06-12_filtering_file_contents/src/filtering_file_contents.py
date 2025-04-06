def filter_solutions():
    with open("src/solutions.csv") as my_file:
        with open("correct.csv", "w") as correct:
            with open("incorrect.csv", "w") as incorrect:
                for line in my_file:
                    line = line.split(";")
                    problem = line[1]
                    result = int(line[2])
                    plus = problem.find('+')
                    if plus > 0:
                        num1 = int(problem[0:plus])
                        num2 = int(problem[(plus + 1):])
                        end = num1 + num2
                    else:
                        minus = problem.find('-')
                        num1 = int(problem[0:minus])
                        num2 = int(problem[(minus + 1):])
                        end = num1 - num2

                    if end == result:
                            line1 = f"{line[0]};{problem};{result}"
                            correct.write(line1+"\n")
                    else:
                            line1 = f"{line[0]};{problem};{result}"
                            incorrect.write(line1+"\n")

if __name__ == "__main__":
    filter_solutions()