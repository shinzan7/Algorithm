from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/13335
N,W,L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0] * W
weight = 0
time = 0

while trucks:
    time += 1

    weight -= bridge[0]
    bridge.pop(0)
    
    # 무게가 최대하중 넘어가지 않으면 추가
    if weight + trucks[0] <= L:
        weight += trucks[0]
        bridge.append(trucks.pop(0))
    else:
        bridge.append(0)

if bridge[-1] != 0:
    time += W

print(time)