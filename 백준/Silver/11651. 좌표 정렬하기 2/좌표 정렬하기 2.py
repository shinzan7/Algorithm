from sys import stdin

input = stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x : (x[1], x[0]))
for x,y in arr:
    print(x,y)