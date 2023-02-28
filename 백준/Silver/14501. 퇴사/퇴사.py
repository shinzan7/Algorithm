from sys import stdin

input = stdin.readline

N = int(input().strip())
days = [0 for _ in range(N)]
money = [0 for _ in range(N)]
for i in range(N):
    d, m = map(int, input().split())
    days[i] = d
    money[i] = m
answer = 0

def dfs(idx, income):
    global answer
    answer = max(answer, income)

    for i in range(idx, N):
        if i+days[i] <= N:
            dfs(i+days[i], income+money[i])

dfs(0,0)
print(answer)