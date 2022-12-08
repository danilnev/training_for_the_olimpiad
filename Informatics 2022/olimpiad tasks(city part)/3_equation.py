numbers = [int(number) for number in input().split()]
result = []
for i in range(-100, 101):
    if numbers[0] * i ** 3 + numbers[1] * i ** 2 + numbers[2] * i + numbers[3] == 0:
        result.append(str(i))
print(' '.join(result))
