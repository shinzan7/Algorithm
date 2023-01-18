import sys

input = sys.stdin.readline

n = int(input().strip())
nums = []

for i in range(n):
    num = int(input().strip())
    nums.append(num)

nums.sort()
diff = 0

for i in range(1, n-1):
    median = nums[i]
    sum1 = nums[0] + median + nums[i+1]
    sum2 = nums[i-1] + median + nums[-1]
    diff = max(diff, abs(median*3 - sum1), abs(median*3 - sum2))

print(diff)