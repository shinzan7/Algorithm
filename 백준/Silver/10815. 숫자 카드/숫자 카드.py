from sys import stdin

input = stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))
cards.sort()
M = int(input().strip())
nums = list(map(int, input().split()))

for n in nums:
    left = 0
    right = N-1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] > n:
            right = mid - 1
        elif cards[mid] < n:
            left = mid + 1
        else:
            result = 1
            break
    print(result, end=' ')