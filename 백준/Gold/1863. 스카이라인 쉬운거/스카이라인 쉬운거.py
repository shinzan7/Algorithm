import sys
from collections import deque

input = sys.stdin.readline
# https://www.acmicpc.net/problem/1863

N = int(input().strip())
answer = 0
stack = deque()

for _ in range(N):
    point, height = map(int, input().split())
    # 이전보다 높은 건물이면 스택에 추가
    if not stack:
        stack.append(height)
        continue
    # 이전보다 낮은 건물이 나오면 +1
    while stack and height < stack[-1]:
        answer += 1
        stack.pop()
    # 스택에는 없지만 남아있는 높이보다 높거나 남아있는 건물이 없으면 추가
    if not stack or stack[-1] < height:
        stack.append(height)
    
# 스택에 남은 건물이 있으면 +1
while stack:
    if stack[-1] > 0:
        answer += 1
    stack.pop()

print(answer)