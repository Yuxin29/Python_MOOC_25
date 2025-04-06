student = int(input("How many students on the course?"))
group = int(input("Desired group size?"))
extra = student % group
whole = student // group
if extra > 0:
    print(f"Number of groups formed: {whole + 1}")    
else:
    print(f"Number of groups formed: {student // group}")