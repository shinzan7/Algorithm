from sys import stdin

input = stdin.readline

N,K = map(int, input().split())
arr = list(map(int, input().split()))
robot = [False for _ in range(N)]

zero = 0

def rail():
    arr.insert(0, arr.pop())
    robot.insert(0, robot.pop())
    if robot[N-1]:
        robot[N-1] = False

def robot_move():
    global zero
    for i in range(N-2, 0, -1):
        if robot[i] and not robot[i+1] and arr[i+1] != 0:
            arr[i+1] -= 1
            if arr[i+1] == 0:
                zero += 1
            robot[i] = False
            robot[i+1] = True
    robot[N-1] = False

def load_robot():
    global zero
    if arr[0] != 0:
        arr[0] -= 1
        if arr[0] == 0:
            zero += 1
        robot[0] = True

count = 0
while True:
    count += 1
    rail()
    robot_move()
    load_robot()
    if zero >= K:
        break
print(count)