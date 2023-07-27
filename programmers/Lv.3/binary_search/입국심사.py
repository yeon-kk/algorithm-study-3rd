# 초반 풀이: times 원소의 배수들을 모두 배열에 포함하고 정렬해서 index로 찾기
# 그런데 1,000,000,000을 보고 의도한 풀이는 탐색일 것이라는 생각이 들었다.
# 이진탐색을 한다면 max값을 어떻게 설정해야 할지가 가장 고민된 부분이었다.
# 이 부분은 times의 가장 최대 시간에 n을 곱한 값으로 지정.
# 걸리는 시간의 '최솟값'이 이진 탐색으로 풀이하는데 핵심 키워드였다.
def cal(times,t):
    return sum([t//time for time in times])
    
def solution(n, times):
    start, end = 1, max(times)*n
    while start<=end:
        mid = (start + end)//2
        result=cal(times,mid)
        if result >= n:
            if mid>1 and cal(times,mid-1) < n:
                break
            end = mid-1
        else:
            start = mid+1
                
    return mid