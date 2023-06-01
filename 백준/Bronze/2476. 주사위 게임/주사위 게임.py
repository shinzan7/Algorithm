from sys import stdin

input = stdin.readline

N = int(input().strip())

def get_score(a,b,c):
    same = 0
    if a == b:
        same += 1
    if b == c:
        same += 1
    if c == a:
        same += 1

    if same == 3:
        return 10000 + a * 1000
    elif same == 1:
        num = 0
        if a == b:
            num = a
        else:
            num = c
        return 1000 + num * 100
    else:
        return max(a,b,c) * 100

answer = 0
for _ in range(N):
    a,b,c = map(int, input().split())
    answer = max(answer, get_score(a,b,c))
print(answer)