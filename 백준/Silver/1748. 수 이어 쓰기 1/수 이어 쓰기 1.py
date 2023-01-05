import sys


n = sys.stdin.readline().strip()
num = len(n)
n = int(n)

answer = 0

for i in range(1, num):
    answer += 9 * 10 ** (i-1) * (i)

answer += (n - 10**(num-1) + 1) * num

print(answer)