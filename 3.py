# class Bird:
#     def __init__(self, name, age, color):
#         self.name = name 
#         self.age = age
#         self.color = color

#     def fly(self):
#         return f"{self.name} can fly" 


# #This is and example of single inheritance
# class Cookoo(Bird):
#     def sing(self):
#         return f"{self.name} can sing"

# b1 = Bird("Sparrow", 3, "Brown")
# b2 = Cookoo("Coockoo", 4, "Black")
# print(b2.name)
# print(b2.fly())
# print(b2.sing())


# Multiple Inheritance

class A:
    def __init__(self, name):
        self.name = name

    def sing(self):
        return f"{self.name} can sing"

    def dance(self):
        return f"{self.name} can Dance"

    def cook(self):
        return f"{self.name} can Cook"

class B:
    def drive(self):
        return "B can drive"

    def write(self):
        return "B can write"

    def listen(self):
        return "B can listen"

class C(A,B):
    def play():
        return "C can play"

c1 = C("C");
print(c1.dance())
print(c1.write())