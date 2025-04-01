# # # # # # # def outer_function():
# # # # # # #     print("This is the outer function.")

# # # # # # #     def inner_function():
# # # # # # #         print("This is the inner function.")

# # # # # # #     inner_function()

# # # # # # # outer_function()

# # # # # # def out():
# # # # # #     print("This is a outer funtion")

# # # # # #     def inner():
# # # # # #         print("This is a inner funtion")
# # # # # #     inner()
# # # # # # out()

# # # # # def cube(n):
# # # # #     return n*n*n
# # # # # def result(func,value):
# # # # #     return func(value)
# # # # # # r=cube(3)
# # # # # # print(r)
# # # # # print(result(cube,10))

# # # # def outer():
# # # #     def inner():
# # # #         print("This is in.")
# # # #     return inner
# # # # result = outer()
# # # # print(result())

# # # square = lambda x:x+x
# # # print(square(4))

# # from math import sqrt,pow
# # print(sqrt(9))
# # print(pow(2,8))
# import math as m
# print(m.pow(3,14))



import mymodule
print(dir(mymodule)) 