# class Paytm:
#     def __init__(self, name):
#         self.name = name

#     def payment(self):
#         return "Doing payment from paytm"

# class Debit_card(Paytm):
#     def payment(self):
#         return "Doing payment from debit_card"


# class Credit_card(Paytm):
#     def payment(self):
#         return "Doing payment from credit_card"

# c = Credit_card("Arjun")
# d = Debit_card("Mohit")
# print(c.payment())
# print(d.payment())

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def calculate_marks(self, phy_marks, chem_marks, maths_marks):
#         return phy_marks+chem_marks+maths_marks


# class Amit(Student):
#     def calculate_marks(self, phy_marks, chem_marks, maths_marks, honour_marks):
#         return phy_marks+chem_marks+maths_marks +honour_marks


# A = Amit("Amit", 20)
# print(A.calculate_marks(80, 90, 100))