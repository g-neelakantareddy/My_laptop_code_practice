class Student:
    school = "A,P Model School"

    def __init__(self, name, classs):
        self.name = name
        self.classs = classs

    def info(self):
        return f"{self.name} is studying {self.classs} in {Student.school}"


s1 = Student("Neela", "8th")
s2 = Student("Haritha", "7th")
print(s1.info())
print(s2.info())

