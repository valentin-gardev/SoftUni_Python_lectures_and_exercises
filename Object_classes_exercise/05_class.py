class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1
            self.get_average_grade()

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.students)
        return float(f'{average_grade:.2f}')

    def __repr__(self):
        average_grade = self.get_average_grade()

        return f'The students in {self.name}: {", ".join(self.students)}. Average grade: {average_grade}'

#Test
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
