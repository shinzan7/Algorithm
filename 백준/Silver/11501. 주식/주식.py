from sys import stdin

input = stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    arr = list(map(int, input().split()))
    
    # 뒤에서부터 검사하면서 최고점보다 낮은값을의 이익을 계산한다.
    # 고점보다 높은 값이 나오면 갱신한다.
    answer = 0
    maxx = arr[-1]
    for i in range(N-1, -1, -1):
        if maxx > arr[i]:
            answer += maxx - arr[i]
        else:
            maxx = arr[i]
    
    print(answer)