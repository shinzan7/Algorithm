def solution(s):
    answer = 0
    
    word = ""
    
    first = 0
    other = 0
    
    for i in s:
        print(i + " : " + str(answer))
        
        if(first == 0):
            word = i
            first = 1
            continue
        if(first == other):
            answer += 1
            first = 0
            other = 0
        else:
            if(word == i):
                first += 1
            else:
                other += 1
                if(first == other):
                    answer += 1
                    first = 0
                    other = 0
    if(first != other):
        answer += 1
    
    return answer