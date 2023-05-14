from sys import stdin

input = stdin.readline

N = int(input().strip())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

current = city[0]
cost = 0
for i in range(N-1):
    if current > city[i]:
        current = city[i]
    cost += current * road[i]

print(cost)