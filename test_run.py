# Initialize the list to store the total scores for each student
total_scores = []

# Number of students
num_students = int(input("Enter the number of students: "))

# Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Collect scores for each student
for i in range(num_students):
    print(f"\nEntering scores for Student {i + 1}")
    total_score = 0
    for j in range(num_subjects):
        score = float(input(f"Enter score for subject {j + 1}: "))
        total_score += score
    total_scores.append(total_score)

# Calculate and print the average score for each student
print("\nAverage scores for each student:")
for i in range(num_students):
    average_score = total_scores[i] / num_subjects
    print(f"Student {i + 1}: {average_score:.2f}")