from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/14658

R, C, L, K = map(int, input().split())
stars = []
result = 0
for _ in range(K):
    x,y = map(int, input().split())
    stars.append((x,y))

# i의 x좌표와 j의 y좌표의 값에 L을 더하여 그 사이에 있는 별이 몇개인지 k를 돌리면서 찾기
for i in range(K):
    for j in range(K):
        cnt = 0
        for k in range(K):
            if stars[i][0] <= stars[k][0] <= stars[i][0]+L and stars[j][1] <= stars[k][1] <= stars[j][1]+L:
                cnt += 1
        result = max(result, cnt)

print(K-result)