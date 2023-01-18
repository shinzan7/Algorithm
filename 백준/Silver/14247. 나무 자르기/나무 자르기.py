import sys

input = sys.stdin.readline

N = int(input().strip())
tree = list(map(int, input().split()))
grow = list(map(int, input().split()))
index = list(range(N))

index = sorted(index, key=lambda i: grow[i])

answer = 0
for i in range(N):
    idx = index[i]
    answer += tree[idx] + i * grow[idx]

print(answer)