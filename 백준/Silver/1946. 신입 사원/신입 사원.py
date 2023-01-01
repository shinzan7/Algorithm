import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = []

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        arr.append((a, b))
    arr = sorted(arr)

    # 1명일때는 바로 다음 테스트케이스로
    if(N == 1):
        print(1)
        continue

    cnt = 1
    cutline = arr[0][1]
    for i in range(1, N):
        # 순위가 둘 다 낮지 않다면
        if(arr[i][1] < cutline):
            cutline = arr[i][1]
            cnt += 1
    print(cnt)