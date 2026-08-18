# class Bird:
#     def __init__(self, name, age, color):
#             This variable is called Public
#         self.name = name 
#         self.age = age
#         self.color = color
#     #decorator
#     @staticmethod
#     def fly():
#         return "Bird can fly"   


# b1 = Bird("Sparrow", 2, "Brown")
# b2 = Bird("Coockoo", 3, "Black")
# # print(Bird.fly())
# print(b1.fly())

#Abstraction

# class Car:
#     def __init__(self):
#         acc = False
#         cluth = False
#         gear = False
#         brk = False;

#     def run(self):
#         acc = True
#         cluth = True
#         gear = True
#         if(acc == True and cluth == True and gear==True):
#             return "Car is running"

# c1 = Car();
# print(c1.run())

#Private method

class Balance:
    def __init__(self, balance, name, pin):
        self.__account_balance = balance
        self.name = name
        self.pin = pin

    def show_Balance(self):
        if(self.pin==321):
            return f"Your Account balance is {self.__account_balance}"
        else:
            return "Your pin is not correct"
        

b1 = Balance(50000, "Xyz", 123)
print(b1.show_Balance())