from sys import stdin

input = stdin.readline

N = int(input().strip())
idx = 0
members = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    members.append((age,idx,name))
    idx += 1

members.sort(key = lambda x : (x[0], x[1]))

for age, idx, name in members:
    print(age, name)