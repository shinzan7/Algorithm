from sys import stdin
from collections import deque

input = stdin.readline

N,d,k,c = map(int, input().split())
arr = []
visit = [0 for _ in range(d+1)]
for _ in range(N):
    arr.append(int(input().strip()))

dish = deque()
count = 0
for i in range(N-k, N):
    if visit[arr[i]] == 0:
        count += 1
    visit[arr[i]] += 1
    dish.append(arr[i])

answer = count
if visit[c] == 0:
    answer += 1
for i in range(N-2):
    left = dish.popleft()
    visit[left] -= 1
    if visit[left] == 0:
        count -= 1
    
    right = arr[i]
    if visit[right] == 0:
        count += 1
    visit[right] += 1
    dish.append(right)
    
    if visit[c] == 0:
        answer = max(answer, count+1)
    else:
        answer = max(answer, count)
        
print(answer)