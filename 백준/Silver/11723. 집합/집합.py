from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/11723
M = int(input().strip())
s = set()

for _ in range(M):
    order = input().split()
    
    if len(order) == 1:
        if order[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue

    num = int(order[1])

    if order[0] == 'add':
        s.add(num)
    elif order[0] == 'remove':
        s.discard(num)
    elif order[0] == 'check':
        print(1 if num in s else 0)
    elif order[0] == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)