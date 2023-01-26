import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
result = 0

def calculate(x):
    sum = 0
    for i in range(N-1):
        sum += abs(x[i] - x[i+1])
    return sum

def dfs(visit, num):
    global result
    if len(num) == N:
        result = max(calculate(num), result)
        return
    
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            num.append(arr[i])
            dfs(visit, num)
            visit[i] = False
            num.pop()

v = [False for _ in range(N)]
dfs(v, [])
print(result)