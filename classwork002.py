# import random
#
# secret = random.randint(1,10)
# while True:
#     num = int(input("Please guess a number: "))
#     if num == secret:
#         break
# print("You got it", secret)

# counter = 0
# while True:
#     ans = input("Please enter yes or no: ")
#     if ans == "0":
#         break
#     else:
#         counter += 1
# print(counter)
#
# substring = "hello_world"
# for i in substring:
#     print(i)
# word = "Hello".upper()
# print(word)
# print(word.lower())
# for i in range(5):
#     print("*"*5)
#
# print()
#
# for i in range(1,6):
#     print("*"*i)
#
# print()
#
# times = 0
# for i in range(10):
#     for j in range(4-times):
#         print(" ", end="")
#     if i % 2 != 0:
#         times += 1
#         for k in range(i):
#             print("*",end="")
#     print()
#
# def add(n1,n2):
#     return n1 + n2
# def minus(n1,n2):
#     return n1 - n2
# def times(n1,n2):
#     return n1 * n2
# def divide(n1,n2):
#     return n1 / n2
#
# while True:
#     n1 = int(input("Please enter the first number: "))
#     symbol = input("Please enter a symbol, +, -, *, /: ")
#     n2 = int(input("Please enter the first number: "))
#
#     if symbol == "+":
#         print(add(n1,n2))
#     elif symbol == "-":
#         print(minus(n1,n2))
#     elif symbol == "*":
#         print(times(n1,n2))
#     elif symbol =="/":
#         print(divide(n1,n2))
#     else:
#         print("Invalid input")
#     ans = int(input("Do you want to continue? yes press: 1, no press: 0: \n"))
#     if ans == 0:
#         break
import pygame
print(pygame.__version__)
