a = int(input())
b = int(input())
num1 = 0
num2 = 0
if (a + b) % 3 != 0:
    print(-1)
else:
    if a > b:
        while a > 2:
            num1 += 1
            a -= 2
            b -= 1
        num2 += b // 2
    else:
        while b > 2:
            num2 += 1
            b -= 2
            a -= 1
        num1 += a // 2
    print(num1, num2)
