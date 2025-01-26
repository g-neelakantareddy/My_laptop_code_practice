class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop("HP", "Ryzen", "16gb")

    def show(self):
        print(self.name, self.roll_no)

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Neela", "4")
s2 = Student("Hari", "24")
s2.show()
s2.lap.show()
