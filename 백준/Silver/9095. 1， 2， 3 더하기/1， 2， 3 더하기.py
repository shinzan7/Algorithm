from sys import stdin

# stdin = open("input.txt", "rt")
N = int(stdin.readline())

def dfs(target, summ):
    global cnt
    if(summ == target):
        cnt += 1
        return
    elif(summ > target):
        return

    for i in range(1,4):
        dfs(target ,summ + i)

for t in range(N):
    cnt = 0
    target = int(stdin.readline())
    dfs(target, 0)
    print(cnt)