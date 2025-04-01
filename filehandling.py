# # # # # file = open("example.txt","x")
# # # # # file.close()

# # file = open("example.txt","r")
# # content = file.read()
# # print(content)
# # file.close()

# # # file = open("example.txt","a")
# # # file.write("How are you also ask is yourself")
# # # file.close()

# try:
#     num=int(input("Enter a number =  "))
#     result=10/num
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please give proper value")
# else:
#     print(result)
# finally:
#     print("Execution successfully executed")

# class Car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def display(self):
#         print(f"Car brand is {self.brand} and Car color is {self.color}")
# car1=Car("toyota","red")
# car2=Car("Mahindra","white")

# car1.display()
# car2.display()

# class Employee:
#     company="Google"

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# emp1=Employee("Alice",500)
# emp2=Employee("Bob",600)

# print(emp1.company)
# print(emp2.company)

# print(emp1.name)
# print(emp2.salary)

# class dog:
#     def __init__(self,name):
#         self.name=name

#     def bark(self):
#         print(f"{self.name} is barking")

# dog1=dog(input("Enter name of the dog please - "))
# dog1.bark()

# class Animal:
#     species = "Mammal"

#     @classmethod

#     def change_species(cls,new_species):
#         cls.species = new_species
    
# Animal.change_species("Man")
# print(Animal.species)

# class Mathematics:
#     @staticmethod
#     def add(x,y):
#         return x+y
# print(Mathematics.add(5,11))

# class Animal:
#     def __init__(self,name):
#         self.name = name

#         def make_sound(self):
#             print("Some generic sound")
#             print(f"THe name for dog is {self.name}")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woorf ")
#         print(f"THe name for dog is {self.name}")


# dog1=Dog("Sher")
# dog1.make_sound()

# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def get_balance(self):
#         return self.balance
# acc = Bank(5000)
# print(acc.get_balance())

class Bird:
    def make_sound(self):
        print("ABCD")
class Dog:
    def make_sound(self):
        