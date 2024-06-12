class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return 'A'
        elif score > 79:
            return 'B'
        elif score > 69:
            return 'C'
        elif score > 59:
            return 'D'
        else:
            return 'F'

    def add_course(self, course_name, score):
        score = self.calculate_letter_grade(score)
        if course_name in self.__courses:
            self.__courses[course_name].append(score)
        else:
            self.__courses[course_name] = score #dictionaries can be tricky

    def get_courses(self):
        return self.__courses