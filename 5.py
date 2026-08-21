# Hierarchical Inheritance 

# class Parent:
#     def __init__(self, name , height):
#         self.name = name 
#         self.height = height

#     def sing(self):
#         return f"{self.name} can sing"


# class Child(Parent):
#     def dance(self):
#         return f"Child can Dance"

# class SubChild(Parent):
#     def cook(self):
#         return "Subchild can cook"

# s1 = SubChild("Arjun", 150)
# print(s1.sing())


class A:
    def show(self):
        print("I am showing A")

class B(A):
    def show(self):
        print("I am showing A")

class C(B, A):
    def show(self):
        print("I am showing A")

c = C()
c.show()
# print(C.__mro__)
# print(C.mro())

# Hybrid Inheritance