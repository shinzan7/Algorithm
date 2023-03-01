from sys import stdin

input = stdin.readline

N = int(input().strip())
answer = 0
row = [0]*N

def possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(x):
    global answer
    if x == N:
        answer += 1
        return
    for i in range(N):
        row[x] = i
        if possible(x):
            dfs(x+1)

dfs(0)
print(answer)