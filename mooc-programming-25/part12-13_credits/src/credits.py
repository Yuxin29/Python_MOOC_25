from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(courses: list):
    credits = reduce(lambda total_credits, item: total_credits + item.credits, courses, 0)
    return credits
def sum_of_passed_credits(courses: list):
    new_courses = filter(lambda course: course.grade >= 1, courses)
    credits = reduce(lambda total_credits, item: total_credits + item.credits, new_courses, 0)
    return credits
def average(courses: list):
    passed_courses = list(filter(lambda course: course.grade >= 1, courses))
    total_grades = reduce(lambda total_grades, item: total_grades + item.grade, passed_courses, 0)
    ave = total_grades / len(passed_courses)
    return ave
    

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)