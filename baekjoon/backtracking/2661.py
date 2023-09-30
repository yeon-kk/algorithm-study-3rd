N = int(input())
answer = ''.join([ '3' for i in range(N)])
def check(number,n):
    tmp = number + n
    length = len(tmp)//2
    for l in range(length):
        l = l+1
        if tmp[-(l*2):-l]==tmp[-l:]:
            return False
    return True
isEnd = False
def backtracking(number):
    global answer, N, isEnd
    if isEnd: return
    if len(number)==N:
        answer = number
        isEnd = True
        return
    for n in ['1','2','3']:
        if check(number,n):
            backtracking(number+n)
backtracking('')
print(answer)