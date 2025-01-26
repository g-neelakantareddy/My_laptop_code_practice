class Animals:
    def __init__(self, food):
        self.food = food


class Tiger(Animals):
    def __init__(self, food):
        super().__init__(food)

    def eat(self):
        return f"Tiger eats {self.food}"


class Dog(Animals):
    def __init__(self, food):
        Animals.__init__(self, food)

    def eat(self):
        return f"Dog eats {self.food}"


dog = Dog("Chicken")
print(dog.eat())
tiger = Tiger("Meat")
print(tiger.eat())
