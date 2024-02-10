score = []
num_sum = 0.0
for i in range(20):
    name, num, grade = input().split()
    if grade == 'P':
        continue
    else:
        if grade == 'A+':
            grade = 4.5
        elif grade == 'A0':
            grade = 4.0
        elif grade == 'B+':
            grade = 3.5
        elif grade == 'B0':
            grade = 3.0
        elif grade == 'C+':
            grade = 2.5
        elif grade == 'C0':
            grade = 2.0
        elif grade == 'D+':
            grade = 1.5
        elif grade == 'D0':
            grade = 1.0
        elif grade == 'F':
            grade = 0.0
        score.append(float(num) * float(grade))
        num_sum += float(num)

result = sum(score)/num_sum
print('%.6f' %result)