answer = 0
def solution(number):
    global answer
    
    dfs(number, 0, 0, [])
    
    return answer

def dfs(number, cnt, start, arr):
    global answer
    
    if(cnt == 3):
        if(arr[0] + arr[1] + arr[2] == 0):
            answer += 1
        return
    
    for i in range(start, len(number)):
        arr.append(number[i])
        dfs(number, cnt+1, i+1, arr)
        arr.pop()