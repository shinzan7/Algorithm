def solution(clothes):
    answer = 1
    s = {}
    for c in clothes:
        if c[1] not in s:
            s[c[1]] = 1
        else:
            s[c[1]] += 1
    arr = []
    for i in s:
        arr.append(s[i])
    for a in arr:
        answer *= a + 1
    answer -= 1
    
    return answer