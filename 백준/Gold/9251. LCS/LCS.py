from sys import stdin

input = stdin.readline

first = input().strip()
second = input().strip()

R = len(first) + 1
C = len(second) + 1

arr = [[0 for _ in range(C)] for _ in range(R)]

def lcs(r,c):
    global first, second
    if first[r-1] == second[c-1]:
        return arr[r-1][c-1] + 1
    else:
        return max(arr[r-1][c] , arr[r][c-1])

for r in range(1, R):
    for c in range(1, C):
        arr[r][c] = lcs(r,c)

print(arr[R-1][C-1])