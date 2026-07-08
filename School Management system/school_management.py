class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)


class ClassRoom:
    def __init__(self, class_name):
        self.class_name = class_name


class School:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.classes = {}
        self.assignments = []

    def add_student(self, key, name):
        self.students[key] = Student(name)

    def add_teacher(self, key, name):
        self.teachers[key] = Teacher(name)

    def add_class(self, key, class_name):
        self.classes[key] = ClassRoom(class_name)

    def assign(self, t_key, s_key, c_key):
        self.assignments.append((t_key, s_key, c_key))

    def show_teacher_view(self):
        print("\n--- TEACHER ---")
        for t_key, teacher in self.teachers.items():
            students = []
            classes = []

            for t, s, c in self.assignments:
                if t == t_key:
                    students.append(self.students[s].name)
                    classes.append(self.classes[c].class_name)

            print(f"\nTeacher: {teacher.name}")
            print("Students:", students)
            print("Classes :", classes)

    def show_student_view(self):
        print("\n--- STUDENT ---")
        for s_key, student in self.students.items():
            teachers = []
            classes = []

            for t, s, c in self.assignments:
                if s == s_key:
                    teachers.append(self.teachers[t].name)
                    classes.append(self.classes[c].class_name)

            print(f"\nStudent: {student.name}")
            print("Teachers:", teachers)
            print("Classes :", classes)
 
school = School()

school.add_teacher("t1", "Ali")
school.add_teacher("t2", "Rehman")

school.add_student("s1", "Ahmed")
school.add_student("s2", "Shoaib")
school.add_student("s3", "Sara")

school.add_class("c1", "BSCS")
school.add_class("c2", "English")

school.assign("t1", "s1", "c1")
school.assign("t1", "s2", "c1")
school.assign("t2", "s3", "c2")
school.assign("t2", "s1", "c2")

school.show_teacher_view()
school.show_student_view()