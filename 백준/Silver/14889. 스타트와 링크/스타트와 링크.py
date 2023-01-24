import sys

input = sys.stdin.readline

N = int(input().strip())
mapp = []
visit = [False for _ in range(N)]
result = 100 * N

for r in range(N):
    arr = list(map(int, input().split()))
    mapp.append(arr)

def dfs(cnt, is_start, idx):
    global result
    if cnt == N/2:
        start = 0
        link = 0
        for r in range(N):
            for c in range(N):
                if r == c:
                    continue
                if is_start[r] and is_start[c]:
                    start += mapp[r][c]
                elif not is_start[r] and not is_start[c]:
                    link += mapp[r][c]
        
        if start != 0 and link != 0:
            result = min(result, abs(start - link))
        return
    
    for i in range(idx, N):
        is_start[i] = True
        dfs(cnt+1, is_start, i+1)
        is_start[i] = False

dfs(0, visit, 0)

print(result)