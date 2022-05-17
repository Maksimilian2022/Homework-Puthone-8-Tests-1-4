class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def put_rate_lector (self, courses_in_progress, grade, lector):
        if isinstance(lector, Lector) and courses_in_progress in lector.course_doing:
            lector.grade_lectors.append(grade)
            print(lector.grade_lectors_list)
        else:
            print('Что-то не верно')

    def __str__(self, name, surname):
        print('Имя: ', name)
        print('Фамилия :', surname)
        if isinstance(self, Student) and len(self.grades) >= 2:
            print('Средняя оценка за домашнее задание: ', sum(self.grades) / len(self.grades))
        else:
            print(self.grades)
        print(self.finished_courses)
        return ' '

    def top_students(self, students, subject):
        sum_student = 0
        sum_students = 0
        for student in students:
            if isinstance(student, Student) and len(students) >= 1 and subject in self.courses_in_progress:
                sum_students += 1
                sum_student += sum(student.grades) / len(student.grades)
            else:
                print('Ошибка')

        print(sum_student/sum_students)






class Student2(Student):
    None

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
            print('Средняя оценка за лекцию: ', sum(self.grade_lectors) / len(self.grade_lectors))
        else:
            print('Ошибка')

    def top_lector(self, lectors, subject):
        sum_lector = 0
        sum_lectors = 0
        for lector in lectors:
            if isinstance(lector, Lector) and len(lectors) >= 1 and subject in self.course_doing:
                sum_lectors += 1
                sum_lector += sum(lector.grade_lectors) / len(lector.grade_lectors)
            else:
                print('Ошибка')

        print(sum_lector/sum_lectors)
        return ' '


class Reviewer(Mentor):
    def put_rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades += [grade]
        else:
            print('Ошибка')
            return ' '


    def __str__(self, name, surname):
        print('Имя: ', name)
        print('Фамилия :', surname)
        return ' '



cool_lector = Lector('Python')

# Здесь мы создаём экзймпляр класса Student2 и прогоняем его по методам
student2 = Student2('R', 'Em', 'my_gender')
student2.add_courses('Python')
student2.grades += [6]
student2.put_rate_lector('Python', 7.5, cool_lector)
student2.put_rate_lector('Python', 7, cool_lector)
print(cool_lector.grade_lectors)
print(student2.__str__('R', 'Em'))
student3 = Student('Student', '3', 'gender')
student2.courses_in_progress= ['Python']
student3.courses_in_progress = ['Python']

student3.grades += [8]
student2.top_students([student3, student2], 'Python')
print(student2.grades, student3.grades)

# Здесь мы создаём экзймпляр класса Reviever и прогоняем его по методам
print('#################')
cooll_reviever = Reviewer('Cool', 'reviever')
cooll_reviever.courses_attached += ['C++']
student2.courses_in_progress += ['C++']
cooll_reviever.put_rate(student2, 'C++', 8.9)
print(student2.grades)

# Здесь мы создаём экзймпляр класса Lector и прогоняем его по методам

print('#####################')
cool_lector.__str__('Cool', 'Lector')
norm_lector = Lector('Norm')
norm_lector.grade_lectors += [7, 9]
norm_lector.course_doing += ['Python']
print(norm_lector.top_lector([norm_lector, cool_lector], 'Python'))






