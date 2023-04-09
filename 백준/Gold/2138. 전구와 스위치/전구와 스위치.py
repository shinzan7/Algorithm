from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/2138
N = int(input().strip())
START = input().strip()
END = input().strip()

def change(x):
    if x == '0':
        return '1'
    else:
        return '0'

# 처음 스위치 누르면 1 누르지 않으면 0
def click_start(n):
    cnt = n
    arr = list(START)
    if n == 1:
        arr[0] = change(arr[0])
        arr[1] = change(arr[1])

    for i in range(1, N-1):
        if arr[i-1] != END[i-1]:
            arr[i-1] = change(arr[i-1])
            arr[i] = change(arr[i])
            arr[i+1] = change(arr[i+1])
            cnt += 1
    if arr[-2] != END[-2]:
        arr[-2] = change(arr[-2])
        arr[-1] = change(arr[-1])
        cnt += 1

    if ''.join(arr) != END:
        cnt = 1e9
    return cnt

not_clicked = click_start(0)
clicked = click_start(1)

if not_clicked == 1e9 and clicked == 1e9:
    print(-1)
else:
    print(min(not_clicked,clicked))