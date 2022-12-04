import queue
def solution(k, score):
    answer = []
    q = queue.PriorityQueue()
    
    for i in score:
        q.put(i)
        if(q.qsize() == k+1):
            q.get()
        temp = q.get()
        answer.append(temp)
        q.put(temp)
    
    return answer