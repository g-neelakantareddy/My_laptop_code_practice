class Student:
    sports = "cricket"

    def __init__(self, name):
        self.name = name

    def info(self):
        return f"He is {self.name}"

    @classmethod
    def game(cls):
        return f"he likes {Student.sports}"  # we can't access instance variables in class methods

    @staticmethod
    def read_info(name):  # we can access only class variables
        return f"This is just information about {name}"


s1 = Student("Neela")
print(s1.info())
print(Student.game())
print(Student.read_info("Neela"))
