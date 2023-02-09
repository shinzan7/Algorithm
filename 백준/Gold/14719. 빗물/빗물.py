from sys import stdin

input = stdin.readline

R, C = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
count = 0
# 1층부터 R층까지 검사
for r in range(R):
    count = 0
    # 빗물을 가둘 벽이 있는지 체크하는 boolean
    start = False
    for c in range(C):
        # 현재층 r 이하의 블록이면 임시변수 count = 0
        # 오른쪽으로 가다가 r 이상의 블록을 만나면 count를 answer에 더하기
        if start and arr[c] >= r+1:
            answer += count
            count = 0
        # r 미만의 블록이면 count += 1
        elif start and arr[c] < r+1:
            count += 1
        elif not start and arr[c] >= r+1:
            start = True
        # 열의 범위를 벗어나면 다음 층으로 이동

print(answer)