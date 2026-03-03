student = [(i + 1) for i in range(30)]

for _ in range(28):
    student.remove(int(input()))

print(student[0])
print(student[1])