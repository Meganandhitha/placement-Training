from collections import namedtuple
N = int(input())

columns = input().split()
Student = namedtuple('Student', columns)

total_marks = 0

for _ in range(N):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

average_marks = total_marks / N
print(f"{average_marks:.2f}")
