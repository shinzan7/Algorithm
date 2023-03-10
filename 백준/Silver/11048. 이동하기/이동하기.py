from sys import stdin

input = stdin.readline

R, C = map(int, input().split())
mapp = []
dp = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    mapp.append(list(map(int, input().split())))

dp[0][0] = mapp[0][0]
for r in range(1,R):
    dp[r][0] = mapp[r][0] + dp[r-1][0]
for c in range(1,C):
    dp[0][c] = mapp[0][c] + dp[0][c-1]

for r in range(1,R):
    for c in range(1,C):
        dp[r][c] = max(dp[r-1][c] + mapp[r][c], dp[r][c-1] + mapp[r][c])

print(dp[R-1][C-1])