def solution(s):
    answer = []
    
    dic = dict()
    for i in range(len(s)):
        char = s[i]
        if(dic.get(char) == None):
            answer.append(-1)
            dic[char] = i
        else:
            answer.append(i - dic.get(char))
            dic[char] = i

    return answer