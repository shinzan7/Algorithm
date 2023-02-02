import sys

input = sys.stdin.readline

R,C = map(int, input().split())
answer = 1
if R == 1:
    answer = 1
elif R == 2:
    answer = min(4, (C-1)//2 + 1)
else:
    if C < 7:
        answer = min(4, C)
    else:
        answer = 3 + C - 5
print(answer)