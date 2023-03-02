from sys import stdin

input = stdin.readline

arr = []
zero = []
for i in range(9):
    arr.append(list(map(int, input().split())))

for r in range(9):
    for c in range(9):
        if arr[r][c] == 0:
            zero.append((r,c))

def check_row(r, num):
    for i in range(9):
        if arr[r][i] == num:
            return False
    return True

def check_col(c, num):
    for i in range(9):
        if arr[i][c] == num:
            return False
    return True

def check_square(r,c,num):
    sr = r // 3 * 3
    sc = c // 3 * 3
    for rr in range(3):
        for cc in range(3):
            if num == arr[rr + sr][cc + sc]:
                return False
    return True

def dfs(idx):
    global zero
    if idx == len(zero):
        for a in arr:
            print(*a)
        exit(0)
    
    for i in range(1,10):
        r = zero[idx][0]
        c = zero[idx][1]

        if check_row(r, i) and check_col(c, i) and check_square(r, c, i):
            arr[r][c] = i
            dfs(idx + 1)
            arr[r][c] = 0
dfs(0)