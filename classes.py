### Part 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 12)
student2 = Student("Bob", 13)

# Get the age of student1
student_age = student2.age

print(student_age)

### Part 2
class Student:
    def __init__(self, name, age, current_class):
        self.name = name
        self.age = age
        self.current_class = current_class

    def calculate_average_test_score(self, test_score1, test_score2, test_score3):
        return (test_score1 + test_score2 + test_score3) / 3

student1 = Student("Alice", 12, "7th grade")
student2 = Student("Bob", 13, "8th grade")

# Calculate the average test score of student1
average_test_score = student1.calculate_average_test_score(90, 85, 95)

print(average_test_score)

### Part 3
#class Bird:
#    def __init__(self, name, wings, feathers):
#        self.name = name
#        self.wings = wings
#        self.feathers = feathers
#
#    def fly(self):
#        print(f"{self.name} is flying!")
#
#    def sing(self):
#        print(f"{self.name} is singing!")


#class Owl(Bird):
#    def __init__(self, name, wings, feathers, nocturnal):
#        super().__init__(name, wings, feathers)
#        self.nocturnal = nocturnal
#
#    def hoot(self):
#        print(f"{self.name} is hooting!")


#class Dodo(Bird):
#    def __init__(self, name, wings, feathers, extinct):
#        super().__init__(name, wings, feathers)
#        self.extinct = extinct
#
#    def waddle(self):
#        print(f"{self.name} is waddling!")


#owl = Owl("Owlbert", 2, True)
#dodo = Dodo("Dodsworth", 2, False)

# Owl and Dodo can fly() because they inherit from the Bird class
#owl.fly()
#dodo.fly()

# Owl can hoot() because it is specific to the Owl class
#owl.hoot()

# Dodo can waddle() because it is specific to the Dodo class
#dodo.waddle()
