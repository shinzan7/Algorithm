from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/9935
arr = list(input().strip())
bomb = list(input().strip())

stack = []

for i in range(len(arr)):
    stack.append(arr[i])
    if stack[-1] == bomb[-1] and stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')