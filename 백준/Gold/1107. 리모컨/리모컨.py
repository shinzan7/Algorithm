import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
broken = []
btn = {i for i in range(10)}
if M != 0:
    broken = set(map(int, input().split()))
    btn -= broken

min_cnt = 500000

def find(n):
    global min_cnt

    for b in btn:
        temp = n + str(b)
        min_cnt = min(min_cnt, abs(N - int(temp)) + len(temp))
        if len(temp) < 6:
            find(temp)

if len(btn) != 0:
    find('')
min_cnt = min(min_cnt, abs(N-100))

print(min_cnt)