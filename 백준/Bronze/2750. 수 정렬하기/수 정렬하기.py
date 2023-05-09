from sys import stdin

input = stdin.readline

N = int(input().strip())
nums = []
for _ in range(N):
    nums.append(int(input().strip()))

nums.sort()
for i in nums:
    print(i)