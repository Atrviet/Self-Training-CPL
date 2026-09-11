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
        continue # Ingore 5 and cntinue
    print(i)
    
print("excercise")
# excercise 1: check positive, negative or zero
number = int(input)