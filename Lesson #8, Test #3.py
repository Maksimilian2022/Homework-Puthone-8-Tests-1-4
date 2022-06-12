class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []
        self.grade_avarage = []

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
        print('Фамилия:', surname)
        if isinstance(self, Student) and len(self.grades) >= 2:
            print('Средняя оценка за домашнее задание: ', sum(self.grades) / len(self.grades))
        else:
            print(self.grades)
        print(self.finished_courses)
        return ' '

    def __lt__(self, other):
        student = [self, other]

        if not isinstance(other, Student):
            print('Не сравнимые классы')
            return
        for best in student:
            tuple_grade = (sum(best.grades) / len(best.grades))
            best.grade_avarage.append(tuple_grade)
        return self.grade_avarage[-1] < other.grade_avarage[-1]








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
        self.grade_lectors_avarage = []

    def __str__(self, name, surname):
        print('Имя: ', name)
        print('Фамилия :', surname)
        if isinstance(self, Lector):
            ratyng = sum(self.grade_lectors) / len(self.grade_lectors)
            print('Средняя оценка за лекцию: ', ratyng)
        return ' '

    def __lt__(self, other):
        mentor = [self, other]

        if not isinstance(other, Mentor):
            print('Не сравнимые классы')
            return
        for best in mentor:
            tuple_grade = (sum(best.grade_lectors) / len(best.grade_lectors))
            best.grade_lectors_avarage.append(tuple_grade)
        return self.grade_lectors_avarage[-1] < other.grade_lectors_avarage[-1]



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
advanced_student = Student('Roy', 'Eman', 'your_gender')
advanced_student.put_rate_lector('Python', 9, best_lector )

tim = Reviewer('Fifty ', 'Huyfty')
print(tim.__str__('Fifty ', 'Huyfty'))

print(best_lector.__str__('Ruoy', 'Eman'))

advanced_student.grades = 5, 6
print(advanced_student.__str__('Ruoy', 'Eman'))
norm_student = Student('Ruoey', 'Iman', 'your_gender')
norm_student.grades = 1, 4
print(advanced_student.grades > norm_student.grades)

print('vsfvfv')
#Попробуем реализовать сравнение по средней оценке
best_student.grades = 7, 9, 8
print(best_student.grades, advanced_student.grades)
print('Сравнение студентов', best_student < advanced_student)
print('Дальше с лекторами ########################')
cool_lector = Lector('Python')
cool_lector.grade_lectors = 7,7
best_lector.grade_lectors = 6,6
best_lector.surname = "JIm"
cool_lector.surname = "Mel"
print(best_lector.grade_lectors)
print(best_lector > cool_lector)