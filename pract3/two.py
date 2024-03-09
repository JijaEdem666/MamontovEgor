class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("Собака", self.name, "села")
    def roll_over(self):
        print("Собака", self.name, "перекатилась")
    def print_self(self):
        print("Собака", self.name, "возраст", self.age)


my_dog = Dog("willie", 6)
my_dog.print_self()
my_dog.sit()
my_dog.roll_over()

my_second = Dog("lucy", 3)
my_second.print_self()
my_second.sit()
my_second.roll_over()