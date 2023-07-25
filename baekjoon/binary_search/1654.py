# 랜선 자르기
# 정말 많은 고민을 했던 문제

# 1. (1) 길이를 기준으로 할 것인지 (2) 개수를 기준으로 할 것인지
# 2. (1) 그렇다면 시작은 가장 작은 것을 (2) 가장 큰 것을 먼저 자른다?
# 3. 2에서 둘 다 가능한 경우들이 각각 존재한다.
# 4. 그리고 길이를 딱 정해서 찾아나간다고 하면, 
# 최대 (2**31)-1번을 반복해서 길이를 선형 탐색해야 하고,
# 거기에 갯수를 구하는 함수도 마찬가지로 반복해야 한다. => 제한 조건안에 실행할 수 없다고 판단했다

# 그러면 탐색 시간을 줄이는 방법을 고민했고 이진 탐색을 떠올렸다.
# - binary_search() 함수를 구현했지만, 재귀 깊이를 초과해서 while문으로 수정
# - 입력된 길이 배열을 반드시 정렬할 필요는 없지만, max값을 찾아야 했다. 해당 값을 가장 끝 값으로 지정해주었다.
# - 배열을 만들어서 1부터 랜선의 가장 긴 값을 배열에 담아 탐색할까 했지만
# - 배열과 index로 접근하지 않고, 값으로만 접근하면 메모리를 절약할 수 있을 것이라 생각했다.
# - while문으로 바꾸면서 종료조건 whle(start <= end) 설정

# 착각했던 부분
# - endpoint가 있으면 안된다. end로 줄어든 index를 관리해야 한다.
# - 종료조건

# 탐색을 먼저 떠올리고,
# 특정 조건에 맞는 하나를 탐색하는 것이라고 인지해야 이분탐색을 떠올릴 수 있을 것 같다.

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
arr.sort()

def checkCount(length):
    global arr
    return sum([(value // length) for value in arr])

def solution(N, arr):
    # 탐색으로 길이를 반씩 나눠가며 찾는다
    # 랜선을 찾은 길이로 나눈다
    # 갯수를 N과 비교한다
    # 갯수가 N보다 작은 경우 binary_srarch를 길이가 작은 방향으로 수행한다
    # 갯수가 N보다 큰 경우 binary_search를 길이가 긴 방향으로 수행한다.

    find, start, end = 0, 1, arr[-1]
    while start <= end:
        mid = (start + end) // 2
        count = checkCount(mid)
        if count == N:
            find = mid
            if (mid+ 1 <= end) and checkCount(mid+1)!=N:
                break
            start = mid + 1
        elif count > N:
            find = mid
            start = mid + 1
        else:
            end = mid - 1
    return find

print(solution(N, arr))