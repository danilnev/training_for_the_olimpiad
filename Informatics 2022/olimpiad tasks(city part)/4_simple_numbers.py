n = int(input())
nums = [i for i in range(n + 1)]
nums[1] = 0
result = []

i = 2
while i <= n:
    if nums[i] != 0:
        result.append(str(nums[i]))
        for j in range(i, n+1, i):
            nums[j] = 0
    i += 1
if result:
    print(' '.join(result))
else:
    print('Absent')
