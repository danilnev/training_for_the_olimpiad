k = int(input())
n = int(input())
result = n % k
if n <= k:
    if (n * 2) < k:
        print(n)
    else:
        print(k - n)
elif (result * 2) <= k:
    print(result)
else:
    print(k - result)
