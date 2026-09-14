import csv
import pandas as pd
import numpy as np


class Student:
    def __init__(self, id, name, python_score, math_score):
        self.id = id
        self.name = name
        self.python_score = python_score
        self.math_score = math_score
        
    def calculate_avg_score(self):
        return (self.python_score + self.math_score) / 2
    
    def get_perform(self):
        avg = self.calculate_avg_score()
        if avg >= 90:
            return "Excellent"
        elif avg >= 75:
            return "Good"
        elif avg >= 60:
            return "Average"
        else:
            return "Poor"
    
    def display_info(self):
        print(f"Student ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Average Score: {self.calculate_avg_score()}")
        print(f"Performance: {self.get_perform()}")   
        print("---")

students = []

with open('Week 2/Lession 4/Student.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        student = Student(
            row['id'],
            row['name'],
            float(row['python_score']),
            float(row['math_score'])
        )
        students.append(student)

for student in students:
    student.display_info()
    
df = pd.read_csv('Week 2/Lession 4/Student.csv', encoding='utf-8-sig')
print(df)

python_scores = np.array([
    student.python_score
    for student in students
])

math_scores = np.array([
    student.math_score
    for student in students
])

print("Python Scores:", python_scores)
print("Math Scores:", math_scores)

df['average_score'] = (python_scores + math_scores) / 2

def average_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Poor"

df['performance'] = df['average_score'].apply(average_score)

print(df)