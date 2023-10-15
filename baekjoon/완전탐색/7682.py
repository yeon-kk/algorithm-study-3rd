import sys
board = []
answer = []
def checkBingo(board):
    lines= [(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(1,4,7),(0,3,6),(2,5,8)]
    result = {'X':0,'O':0}
    for (x,y,z) in lines:
        if board[x] == '.' or board[y] == '.' or board[z] == '.': continue
        if board[x] == board[y] == board[z] :
            result[board[x]] +=1
    return result
while True:
    board = list(sys.stdin.readline().rstrip())
    if len(board)==3: break
    result = checkBingo(board)
    xCount,oCount =result['X'],result['O']
    tmp = {'X':0, 'O':0,'.':0}
    for elem in board:
        tmp[elem]+=1
    if tmp['X']-tmp['O']==1 and xCount >=1 and oCount==0:
        answer.append('valid')
    elif tmp['X']==tmp['O'] and oCount==1 and xCount==0:
        answer.append('valid')
    elif tmp['X']==5 and tmp['O']==4 and xCount ==0 and oCount==0:
        answer.append('valid')
    else:
        answer.append('invalid')
print('\n'.join(answer))