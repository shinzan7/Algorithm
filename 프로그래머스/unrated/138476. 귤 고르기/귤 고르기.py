import collections

def solution(k, tangerine):
    answer = 0
    
    c = collections.Counter(tangerine).most_common()
    n = 0
    
    for i in range(len(c)):
        n += c[i][1]
        answer += 1
        if(n >= k):
            break
    
    return answer