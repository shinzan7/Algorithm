from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
people = {}
for _ in range(N):
    name = input().strip()
    people[name] = 1

answer = []
for _ in range(M):
    name = input().strip()
    if people.get(name):
        answer.append(name)

answer.sort()
print(len(answer))
for a in answer:
    print(a)