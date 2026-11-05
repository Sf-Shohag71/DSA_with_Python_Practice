if __name__ == '__main__':
    students = []
    print("Enter total students: ")
    for i in range(int(input())):
        print(f"Enter student's name {i}: ")
        name = input()
        print(f"Enter student's mark {i}: ")
        mark = float(input())
        students.append([name, mark])

    sortedGrade = sorted(set(student[1] for student in students))
    secondLowestMark = sortedGrade[1]
    secondLowestName = sorted(student[0] for student in students if student[1] == secondLowestMark)

    for i in secondLowestName:
        print(i)