import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * N
prefix[0] = arr[0]
for i in range(1,N):
    prefix[i] = prefix[i-1] + arr[i]

cnt = {}
result = 0

for i in range(N):
    target = prefix[i] - K

    if target in cnt:
        result += cnt[target]
    # 0 ~ i까지의 합이 K인 경우
    if target == 0:
        result += 1
    # 양수 index부터 시작하여 i까지의 합이 K인 경우
    if prefix[i] not in cnt:
        cnt[prefix[i]] = 0
    cnt[prefix[i]] += 1

print(result)