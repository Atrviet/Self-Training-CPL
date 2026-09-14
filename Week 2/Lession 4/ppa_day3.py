# OOP

class Student:
    def __init__(self, student_id, name, python_score, math_score):
        self.student_id = student_id
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
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Average Score: {self.calculate_avg_score()}")
        print(f"Performance: {self.get_perform()}")   
        
student1 = Student(
    "S01",
    "Name",
    85,
    90
)

student1.display_info()