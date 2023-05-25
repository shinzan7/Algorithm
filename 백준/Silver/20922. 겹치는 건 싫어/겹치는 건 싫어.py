from sys import stdin

input = stdin.readline

N, K = map(int, input().split())

l, r = 0, 0
nums = [0] * 100001
answer = 1
arr = list(map(int, input().split()))
nums[arr[0]] = 1

while True:
    
    if r == N-1:
        break

    r += 1
    nums[arr[r]] += 1
    if nums[arr[r]] > K:
        while nums[arr[r]] > K:
            nums[arr[l]] -= 1
            l += 1
    else:
        answer = max(answer, r-l+1)

print(answer)