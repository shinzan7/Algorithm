import collections
def bfs(maps):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    R = len(maps)
    C = len(maps[0])
    is_visit = [[False for col in range(C)] for row in range(R)]
    q = collections.deque([])
    is_visit[0][0] = True
    cnt = 1
    q.appendleft([0,0,0])
    
    while(q):
        cur = q.pop()
        
        # 도착
        if(cur[0] == R-1 and cur[1] == C-1):
            return cur[2] + 1
        
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if(nr>=0 and nc>=0 and nr<R and nc<C and not is_visit[nr][nc] and maps[nr][nc] == 1):
                is_visit[nr][nc] = True
                q.appendleft([nr, nc, cur[2] + 1])
        
    # 못감
    return -1

def solution(maps):
    answer = bfs(maps)
    
    return answer