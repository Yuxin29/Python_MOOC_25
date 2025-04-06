class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade
    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    acceptions = filter(lambda attemp: attemp.grade >= 1, attempts)
    return acceptions

def attempts_with_grade(attempts: list, grade: int):
    acceptions_with_grades = filter(lambda attemp: attemp.grade == grade, attempts)
    return acceptions_with_grades

def passed_students(attempts: list, course: str):
    passed = list(filter(lambda attemp: attemp.course_name == course and attemp.grade > 0, attempts))
    names = map(lambda t: t.student_name, passed)
    names_alpha = sorted(names)
    return names_alpha

if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)