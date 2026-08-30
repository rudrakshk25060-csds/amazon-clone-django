# Concept of Super() method
# class Parent:
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight

#     def sing(self):
#         return f"{self.name} can sing"


# class Child(Parent):
#     def __init__(self, name, height, weight, eyes_color):
#         self.eyes_color = eyes_color
#         super().__init__(name, height, weight)

#     def dance(self):
#         return f"{self.name} can dance"

# c1 = Child("Mohit", 180, 85, "brown")
# print(c1.name)
# print(c1.sing())