import sys

input = sys.stdin.readline

T = int(input().strip())

def find_distance(a,b,x,y):
    return (abs(a-x)**2 + abs(b-y)**2)**(1/2)

for _ in range(T):
    a,b,r1,x,y,r2 = map(int, input().split())

    if a == x and b == y: # 원의중심이 같은경우
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    dist = find_distance(a,b,x,y)
    
    # 떨어진 경우
    if dist > r1 + r2: 
        print(0)
    # 접한 경우
    elif dist == r1 + r2: 
        print(1)
    # 내부원이 접한경우
    elif dist + min(r1,r2) == max(r1,r2): 
        print(1)
    # 원 내부에 있는경우
    elif dist + min(r1,r2) < max(r1,r2): 
        print(0)
    # 교차
    else: 
        print(2)