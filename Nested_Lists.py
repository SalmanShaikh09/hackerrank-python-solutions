if __name__ == '__main__':
    n = int(input())

    students = []
    
    for i in range(n):
        name = input()
        score = float(input())
        
        students.append([name, score])
      

grades = [student[1] for student in students]

unique_grades = sorted(set(grades))
second_lowest = unique_grades[1]


names = [
    student[0]
    for student in students
    if student[1] == second_lowest
]



names.sort()

for name in names:
    print(name)
