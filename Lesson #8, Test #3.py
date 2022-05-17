class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def put_rate_lector (self, courses_in_progress, grade, lector):
        if isinstance(lector, Lector) and courses_in_progress in lector.course_doing:
            lector.grade_lectors.append(grade)
            print(lector.grade_lectors_list)
        else:
            print('Что-то не верно')

    def __str__(self, name, surname,):
        print('Имя: ', name)
        print('Фамилия :', surname)
        if isinstance(self, Student) and len(self.grades) >= 2:
            print('Средняя оценка за домашнее задание: ', sum(self.grades) / len(self.grades))
        else:
            print(self.grades)
        print(self.finished_courses)
        return ' '

    def student_compare(self, student1):

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, course):
        self.course_doing = [course]
        gr = []
        self.grade_lectors = gr
        self.grade_lectors_list = {course: gr}

    def __str__(self, name, surname):
        print('Имя: ', name)
        print('Фамилия :', surname)
        if isinstance(self, Lector):
            ratyng = sum(self.grade_lectors) / len(self.grade_lectors)
            print('Средняя оценка за лекцию: ', ratyng))
        return ' '


class Reviewer(Mentor):
    def put_rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self, name, surname):
        print('Имя: ', name)
        print('Фамилия :', surname)
        return ' '



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Reviewer('Some', 'Buddy')
cool_mentor2.put_rate(best_student, 'Python', 10)
print(best_student.grades)

best_lector = Lector

best_lector = Lector('Python')
advanced_student = Student('Ruoy', 'Eman', 'your_gender')
advanced_student.put_rate_lector('Python', 9, best_lector )

tim = Reviewer('Fifty ', 'Huyfty')
print(tim.__str__('Fifty ', 'Huyfty'))

print(best_lector.__str__('Ruoy', 'Eman'))

advanced_student.grades = 5, 6
print(advanced_student.__str__('Ruoy', 'Eman'))
norm_student = Student('Ruoey', 'Iman', 'your_gender')
norm_student.grades = 1, 4
print(advanced_student.grades > norm_student.grades)
