N,M=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
find = 0
def checkLength(arr,height):
    result = 0
    for value in arr:
        length = value - height
        if length > 0:
            result+=length
    return result

def binary_search(start,end,M,arr):
    global find
    if start > end:
        return
    mid = (start + end) //2
    length=checkLength(arr,mid)
    if length >= M:
        find = mid
        return binary_search(mid + 1,end,M,arr) 
    else:
        return binary_search(start,mid -1,M,arr)

def solution(arr,M):
    binary_search(1,arr[-1],M,arr)
solution(arr,M)
print(find)