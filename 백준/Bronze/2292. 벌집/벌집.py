from sys import stdin

input = stdin.readline

N = int(input().strip())

k = 1
count = 1
while k < N:
    k += count * 6
    count += 1

print(count)