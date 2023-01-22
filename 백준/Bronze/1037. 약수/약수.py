import sys

input = sys.stdin.readline

num = int(input().strip())
divisor = list(map(int, input().split()))

divisor.sort()

print(divisor[0] * divisor[-1])