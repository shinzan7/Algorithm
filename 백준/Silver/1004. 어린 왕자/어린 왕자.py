from sys import stdin

input = stdin.readline

T = int(input().strip())

def dist(a,b,x,y):
    return ((a-x)**2 + (b-y)**2)**(1/2)

for _ in range(T):
    x1,y1,x2,y2 = map(int, input().split())
    N = int(input().strip())
    answer = 0
    for _ in range(N):
        cx,cy,r = map(int, input().split())
        d1 = dist(x1,y1,cx,cy)
        d2 = dist(x2,y2,cx,cy)

        if (d1-r) * (d2-r) < 0:
            answer += 1
    print(answer)