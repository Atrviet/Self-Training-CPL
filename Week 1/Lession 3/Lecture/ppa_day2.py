
scores = [85, 92, 78, 96, 88, 105, -5, 67, 89, 73]

valid_scores = []
invalid_scores = []

for score in scores:
    if score < 0 or score > 100:
        invalid_scores.append(score)
    else:
        valid_scores.append(score)

print("Valid scores:", valid_scores)
print("Invalid scores:", invalid_scores)

unique_scores = set(valid_scores)
total_unique_scores = len(unique_scores)
total_scores = sum(valid_scores)
highest_score = max(valid_scores)
minimum_score = min(valid_scores)
average_score = total_scores / len(valid_scores)

print("Total unique scores:", total_unique_scores)
print("Total scores:", total_scores)
print("Highest score:", highest_score)
print("Minimum score:", minimum_score)
print("Average score:", average_score)



# defining a function
def get_name(name):
    print(name)

get_name("Hello world")

def sum(a, b):
    return a + b

result = sum(5, 10)
print("Sum:", result)

with open ("data.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")

with open ("data.txt", "r") as file:
    text = file.read()
print(text)

