def solution(answers):
    answer = []
    
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(len(answers)):
        if(s1[i%5] == answers[i]):
            score1 += 1
        if(s2[i%8] == answers[i]):
            score2 += 1
        if(s3[i%10] == answers[i]):
            score3 += 1
    
    if(score1 == score2 == score3):
        return [1,2,3]
    
    if(score1 >= score2 and score1 >= score3):
        answer.append(1)
    if(score2 >= score1 and score2 >= score3):
        answer.append(2)
    if(score3 >= score1 and score3 >= score2):
        answer.append(3)
    
    
    return answer