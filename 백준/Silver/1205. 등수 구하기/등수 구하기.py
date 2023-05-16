from sys import stdin

input = stdin.readline

N, SCORE, P = map(int, input().split())

if N == 0:
    print(1)
else:
    arr = list(map(int, input().split()))
    arr.append(SCORE)
    arr.sort(reverse=True)
    rank = arr.index(SCORE) + 1
    if rank > P:
        print(-1)
    elif N == P and arr[-1] == SCORE:
        print(-1)
    else:
        print(rank)