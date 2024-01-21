from collections import namedtuple

n = int(input())
Student = namedtuple("Student", input().split())
total = 0

for i in range(n):
    f1, f2, f3, f4 = input().split()
    temp = Student(f1, f2, f3, f4)
    total += int(temp.MARKS)

print(round(total/n, 2))
