from sys import stdin

input = stdin.readline

N = int(input().strip())
arr = []
ranking = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x,y))

for i in range(N):
    rank = 1
    x, y = arr[i]
    for j in range(N):
        if i == j:
            continue
        p, q = arr[j]
        if x < p and y < q:
            rank += 1
    ranking.append(rank)

print(*ranking)