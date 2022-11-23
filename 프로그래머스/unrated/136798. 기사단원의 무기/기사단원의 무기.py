def solution(number, limit, power):
    answer = 0
    knights = []
    
    for n in range(1, number + 1):
        knights.append(get_count(n))
    
    for k in knights:
        if(k <= limit):
            answer += k
        else:
            answer += power
    
    return answer

# def get_count(number):
#     count = 0
#     for i in range(1, number + 1):
#         if(number % i == 0):
#             count += 1
#     return count

def get_count(n):
    n = int(n)
    count = 0

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            count += 1
            if (i != (n // i)): 
                count += 1

    return count