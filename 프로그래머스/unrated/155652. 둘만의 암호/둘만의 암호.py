def solution(s, skip, index):
    answer = ''
    alpha = []
    for i in range(97, 123):
        alpha.append(chr(i))
        
    skip_arr = list(skip)
    skip_arr.sort()
    
    for i in range(len(skip)):
        alpha.remove(skip_arr[i])
    
    change = []
    for i in range(len(s)):
        idx = alpha.index(s[i])
        idx += index
        idx %= len(alpha)
        change.append(alpha[idx])
    answer = ''.join(map(str, change))
    
    return answer