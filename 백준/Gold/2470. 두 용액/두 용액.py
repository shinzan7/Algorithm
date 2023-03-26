from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/2470

N = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N-1
answer = [arr[0], arr[N-1], abs(arr[0] + arr[N-1])]

while left < right:
    cur = arr[left] + arr[right]
    # 최솟값 갱신
    if abs(cur) < answer[2]:
        answer = [arr[left], arr[right], abs(cur)]
    if cur > 0:
        right -= 1
    elif cur < 0:
        left += 1
    # 0인 용액 만들면 break
    else:
        break

print(f'{answer[0]} {answer[1]}')