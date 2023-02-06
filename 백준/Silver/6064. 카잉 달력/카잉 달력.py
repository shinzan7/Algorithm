from sys import stdin

input = stdin.readline

T = int(input().strip())

for _ in range(T):
    M,N,x,y = map(int, input().split())
    k = x
    last = M*N
    while True:
        if k > last:
            print(-1)
            break
        if (k-x)%M == 0 and (k-y)%N==0:
            print(k)
            break
        k += M