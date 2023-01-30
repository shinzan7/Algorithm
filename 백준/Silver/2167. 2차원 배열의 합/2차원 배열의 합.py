import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = []
for r in range(R):
    arr.append(list(map(int, input().split())))

psum = [[0 for cols in range(C)] for rows in range(R)]
for r in range(R):
    for c in range(C):
        if r == 0 and c == 0:
            psum[r][c] = arr[0][0]
        elif r == 0 and c != 0:
            psum[r][c] = psum[r][c-1] + arr[r][c]
        elif r != 0 and c == 0:
            psum[r][c] = psum[r-1][c] + arr[r][c]
        else:
            psum[r][c] = arr[r][c] + psum[r-1][c] + psum[r][c-1] - psum[r-1][c-1]

K = int(input().strip())

def minus(x):
    return int(x)-1

for k in range(K):
    a,b,x,y = map(minus, input().split())

    result = 0
    if a == 0 and b == 0:
        result = psum[x][y]
    elif a == 0 and b != 0:
        result = psum[x][y] - psum[x][b-1]
    elif a != 0 and b == 0:
        result = psum[x][y] - psum[a-1][y]
    else:
        result = psum[x][y] - psum[x][b-1] - psum[a-1][y] + psum[a-1][b-1]

    print(result)