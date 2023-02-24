from sys import stdin

input = stdin.readline

arr = list(input().strip())

is_left = True
stack = [arr[0]]
answer = 0
for i in range(1,len(arr)):
    cur = arr[i]
    if cur == '(':
        stack.append(cur)
    elif arr[i-1] == '(':
        stack.pop()
        answer += len(stack)
    elif arr[i-1] == ')':
        answer += 1
        stack.pop()

print(answer)