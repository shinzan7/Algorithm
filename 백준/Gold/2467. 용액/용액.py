from sys import stdin

input = stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
answer = [arr[0], arr[N-1], arr[0] + arr[N-1]]

def find_sol():
    global answer
    for i in range(N):
        cur = arr[i]
        down = i+1
        up = N-1
        while down <= up:
            mid = (down+up)//2
            mix = cur + arr[mid]

            if abs(mix) < abs(answer[2]):
                answer = [cur, arr[mid], mix]
                if answer[2] == 0:
                    return
            if mix < 0:
                down = mid+1
            elif mix > 0:
                up = mid-1

find_sol()
print(f'{answer[0]} {answer[1]}')