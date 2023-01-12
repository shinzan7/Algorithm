from sys import stdin

mapp = [['.' for col in range(3)] for row in range(3)]

def check_num(m):
    o, x = 0, 0
    o_bingo, x_bingo = 0, 0
    cur = '.'
    # 행 빙고검사, O/X 개수세기
    for r in range(3):
        cur = m[r][0]
        for c in range(3):
            if(m[r][c] != cur):
                cur = 'no_bingo'

            if(m[r][c] == 'O'):
                o += 1
            elif(m[r][c] == 'X'):
                x += 1
        if(cur == 'X'):
            x_bingo += 1
        elif(cur == 'O'):
            o_bingo += 1
    # 열 빙고검사
    for c in range(3):
        cur = m[0][c]
        for r in range(3):
            if(m[r][c] != cur):
                cur = 'no_bingo'
        if(cur == 'X'):
            x_bingo += 1
        elif(cur == 'O'):
            o_bingo += 1
    # 대각선 빙고검사
    diag = m[0][0]
    diag2 = m[0][2]
    for i in range(3):
        if m[i][i] != diag:
            diag = 'no_bingo'
        if m[i][2-i] != diag2:
            diag2 = 'no_bingo'
    if(diag == 'X'):
        x_bingo += 1
    elif(diag == 'O'):
        o_bingo += 1
    
    if(diag2 == 'X'):
        x_bingo += 1
    elif(diag2 == 'O'):
        o_bingo += 1
    


    # 개수차이 검사
    if not (x-o == 1 or x-o == 0):
        return False
    
    # 빙고 개수검사
    if x_bingo != 0 and o_bingo != 0:
        return False
    if x_bingo == 0 and o_bingo == 0:
        if x + o == 9:
            return True
        else:
            return False
    if x_bingo > 2 or o_bingo > 1:
        return False
    if x_bingo > 0 and x - o == 1:
        return True
    if o_bingo == 1 and x - o == 0:
        return True
    

while True:
    strr = stdin.readline().strip()
    if strr == 'end':
        break
    idx = 0
    for r in range(3):
        for c in range(3):
            mapp[r][c] = strr[idx]
            idx += 1
    
    if check_num(mapp):
        print('valid')
    else:
        print('invalid')