class Fruit:
    def __init__(self, fruit):
        self.fruit = fruit

    def eat(self):
        return f"Today i'm going to eat {self.fruit}"


fruit_1 = Fruit("Banana")
fruit_2 = Fruit("Apple")
print(fruit_1.eat())
print(fruit_2.eat())
