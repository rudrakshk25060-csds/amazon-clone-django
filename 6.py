# from multipledispatch import dispatch
# class Cat():
#     def speak(self):
#         return "cat can meow"

# class Dog:
#     def speak(self):
#         return "Dog can bark"

# class Calculate:
#     def add(a,b):
#         return a+b

#     def add(a,b,c):
#         return a+b+c

# c = Calculate()
# c.add(2,3)

# class Calculate:
#     @dispatch(int, int)
#     def add(a,b):
#         return a+b
    
#     @dispatch(int, int, int)
#     def add(a,b,c):
#         return a+b+c


# c = Calculate()

# print(c.add(2,3))

# variable length positional Argument
# class Calculate:
#     def add(self ,*params):
#         return sum(params)

#     def subtract(self, *args):
#         num = args[0]
#         for i in args[1:]:
#             num -= i;
#         return num;

# c1 = Calculate()
# print(c1.add(2,3))
# print(c1.subtract(1,2))

# Operator Overloading

# print(2+2)
# print(int.__add__(2,3))
# print(int.__sub__(4,3))

# class Number:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, val):
#         return self.num +val.num

# n = Number(2)
# n1 = Number(5)
# print(n+n1)