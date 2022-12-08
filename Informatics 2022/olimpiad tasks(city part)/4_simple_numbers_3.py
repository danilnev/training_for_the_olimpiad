n = int(input())
array = [i for i in range(n + 1)]
i = 2
array[1] = 0
while i < int(n ** 0.5) + 1:
    if array[i] != 0:
        j = i + i
        while j <= n:
            array[j] = 0
    i += 1
print(array)
