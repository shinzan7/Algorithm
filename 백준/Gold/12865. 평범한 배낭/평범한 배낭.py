from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
bag = []
for _ in range(N):
    bag.append(list(map(int, input().split())))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for r in range(1, N+1):
    w = bag[r-1][0]
    v = bag[r-1][1]
    for c in range(1, K+1):
        if w > c:
            dp[r][c] = dp[r-1][c]
        else:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-w] + v)

print(dp[N][K])