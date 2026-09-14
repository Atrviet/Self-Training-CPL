# if / elif / else
score = 85

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Average")
else:
    print("Needs Improvement")
    
# for loop
for i in range(5):
    print(i)
    
for i in range(1, 6):
    print(i)
    
print("While loop:")
i = 1

while i <= 5:
    print(i)
    i += 1
    
print("break")
for i in range(10):
    if i == 5:
        break
    print(i)
    
print("continue")
for i in range(10):
    if i == 5:
        continue # Ignore 5 and continue
    print(i)
    
print("excercise")

# excercise 1: check positive, negative or zero
number = int(input("enter a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# exercise 2: Check even or odd
number_ex2 = int(input("enter anumber: "))
if number_ex2 % 2 == 0:
    print("even")
else:
    print("odd")
    
# excercise 3: input score and print grade
score = int(input("enter your score: "))
if score >= 8:
    print("Excellent")
elif score >= 6.5:
    print("Good")
elif score >= 5:
    print("Average")
else:
    print("Needs Improvement")
    
# excercise 4: print numbers from 1 to 100
for i in range(1, 101):
    print(i)
    
# excercise 5: print numbers from 1 to 100 break when number is 50
for i in range(1, 101):
    if i == 50:
        break
    print(i)
    
    
# excercise 6: print numbers from 1 to 100 but skip even numbers
for i in range(1, 101):
    if i % 2 == 0:
        continue # Ignore even numbers
    print(i)
    
   

