m, n = [int(num) for num in input().split()]
count = True
if m == 2:
    print(2)
    count = False
numbers = [2]
for i in range(3, n + 1, 2):
    flag = True
    for num in numbers:
        if num >= int(i ** 0.5) + 1:
            break
        elif i % num == 0:
            flag = False
            break
    if flag:
        numbers.append(i)
        if m <= i <= n:
            print(i)
            count = False
if count:
    print('Absent')
