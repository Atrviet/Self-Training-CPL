import sys
import platform

from pathlib import Path


print("OS: ", platform.system())
print("Platform: ", platform.platform())

print("Working Directory: ", Path.cwd())

# Khai báo biến

name = "Trần Văn Việt"
age = 20

print("Hello", name)

# f-string
print(f"Hello {name}")

print(type(name))
print(type(age))


python_score = 10
math_score = 9

avg = (python_score + math_score) / 2

print(avg)
print(type(avg))




#student info: name, age, score, math_score
#print name, age, score, agv

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_score = float(input("Enter your score: "))
student_math_score = float(input("Enter your math score: "))

avg_score = (student_score + student_math_score) / 2

print(f"Student name: {student_name}")
print(f"Student age: {student_age}")
print(f"Student score: {avg_score}")



