# Nested Lists
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# Explanation
# There are  students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

# Use pre-defined lists instead of taking input from user.

name = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
score = [37.2, 37.21, 37.21,  41, 39]
students = []

for i in range(len(name)):
    students.append([name[i], score[i]])

students.sort(key=lambda x: x[1]) # Sort by score
second_lowest_score = sorted(set([student[1] for student in students]))[1] # Get second lowest score
second_lowest_names = sorted([student[0] for student in students 
                              if student[1] == second_lowest_score]) # Get names with second lowest score
for i in second_lowest_names:
    print(i)


# Hackerrank code
# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
        
#     sorted_grade = sorted(set([student[1] for student in students]))
#     # print(sorted_grade)
#     second_lowest_grade = sorted_grade[1]
#     # print(second_lowest_grade)
#     second_lowest_name = sorted([student[0] for student in students 
#     if student[1] == second_lowest_grade])
    
#     for i in second_lowest_name:
#         print(i)

    
