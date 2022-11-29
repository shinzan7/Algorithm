answer = 0
def dfs(summ, cnt, numbers, target):
    global answer
    if(cnt == len(numbers)):
        if(summ == target):
            answer += 1
        return
    
    dfs(summ + numbers[cnt], cnt + 1, numbers, target)
    dfs(summ - numbers[cnt], cnt + 1, numbers, target)

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    
    return answer

