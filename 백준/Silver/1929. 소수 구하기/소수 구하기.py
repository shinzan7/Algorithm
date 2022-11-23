import sys

result = []

M, N = map(int, sys.stdin.readline().split())

if(M == 1):
    M = 2

def get_division(n):
    n = int(n)
    for i in range(2, int(n**(1/2)) + 1):
        if(n % i == 0):
            return False
    return True

for i in range(M, N+1):
    if(get_division(i)):
        print(i)