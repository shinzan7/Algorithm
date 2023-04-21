from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/1011

N = int(input().strip())
distance = []
for _ in range(N):
    a, b = map(int ,input().split())
    num = b-a
    sqrt = int((num)**(1/2))
    answer = 0
    
    # 제곱수 = 제곱근 * 2 - 1
    # 제곱수 중간 넘으면 = 제곱근 * 2
    if num == sqrt**2:
        answer = sqrt * 2 - 1
    elif num <= (sqrt**2 + (sqrt+1)**2) // 2:
        answer = sqrt * 2
    else:
        answer = sqrt * 2 + 1

    print(answer)