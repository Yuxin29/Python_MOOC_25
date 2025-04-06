def points(points_str):
    indivisual_points = points_str.split(" ")
    exam = int(indivisual_points[0])
    exercise = int(indivisual_points[1])
    return (exam, exercise)

def main(exam, exercise):
    result = exam + int(exercise / 10)
    return result

student_number = 0
pass_number = 0
totol_grade = 0
grade5_number = 0
grade4_number = 0
grade3_number = 0
grade2_number = 0
grade1_number = 0
grade0_number = 0
points_str = input("Exam points and exercises completed: ")
while points_str != "":
    tuplee = points(points_str)
    (exam, exercise) = tuplee
    # print(grade(exam, exercise))
    if exam < 10:
        grade0_number += 1
    else:
        if main(exam, exercise) > 14:
            pass_number += 1
        if main(exam, exercise) > 27:
            grade5_number += 1
        elif main(exam, exercise) > 23:
            grade4_number += 1
        elif main(exam, exercise) > 20:
            grade3_number += 1
        elif main(exam, exercise) > 17:
            grade2_number += 1
        elif main(exam, exercise) > 14:
            grade1_number += 1
        else:
            grade0_number += 1
    student_number += 1
    totol_grade += main(exam, exercise)
    points_str = input("Exam points and exercises completed: ")
print("Statistics:")
average_grade = totol_grade / student_number
print(f"Points average: {average_grade:.1f}")
pass_rate = (pass_number / student_number) * 100
print(f"Pass percentage: {pass_rate:.1f}")
print("Grade distribution:")
print(f"  5: {grade5_number * '*'}")
print(f"  4: {grade4_number * '*'}")
print(f"  3: {grade3_number * '*'}")
print(f"  2: {grade2_number * '*'}")
print(f"  1: {grade1_number * '*'}")
print(f"  0: {grade0_number * '*'}")