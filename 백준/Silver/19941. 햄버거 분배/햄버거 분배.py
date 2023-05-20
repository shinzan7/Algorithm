from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
table = list(input().strip())
answer = 0

def search(idx):
    global answer
    start = idx - K if (idx - K >= 0) else 0
    end = idx + K if (idx + K < N) else N-1
    for i in range(start, end+1):
        if table[i] == 'H':
            table[i] = 'E'
            answer += 1
            return

# 왼쪽부터 먹을수 있는 햄버거가 있으면 선택한다.
for i in range(N):
    if table[i] == 'P':
        search(i)

print(answer)