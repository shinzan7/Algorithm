from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * N
prefix[0] = arr[0]
for i in range(1, N):
    prefix[i] = arr[i] + prefix[i-1]
# 1개의 원소로 S 이상이 되는 경우
answer = 100001
if max(arr) >= S:
    answer = 1
# 투 포인터
left = 0
right = 1

# 합이 S보다 작아서 right가 증가하다가 N에 도달하면 멈춤
while right != N:
    if left == right:
        right += 1
        continue
    
    summ = prefix[right] - prefix[left] + arr[left]
    if summ >= S:
        answer = min(answer, right - left + 1)
        left += 1
    else:
        right += 1
# 합을 만드는 것이 불가능한 경우 0 출력
if answer == 100001:
    answer = 0
print(answer)