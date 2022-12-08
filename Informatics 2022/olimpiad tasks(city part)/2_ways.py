length = int(input())
ways = [input().split() for i in range(length)]
result = set()
for i in range(length):
    for j in range(length):
        if ways[i][j] == '1' and (j, i) not in result:
            result.add((i, j))
print(len(result))
