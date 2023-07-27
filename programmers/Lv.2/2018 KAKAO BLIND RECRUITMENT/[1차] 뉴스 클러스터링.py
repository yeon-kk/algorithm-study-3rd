def union(s1,s2):
    #겹치면 큰 값 선택 #안겹치면 포함
    count = 0
    for key,value in s1.items():
        if key in s2:
            count += max(value,s2[key])
        else:
            count +=value
    
    for key,value in s2.items():
        if key not in s1:
            count += value
    return count
    
def intersection(s1,s2):
    #겹치는 것 중 작은 값 선택
    count = 0
    for key,value in s1.items():
        if key in s2:
            count += min(value,s2[key])
    return count
        
def getSet(inputStr):
    dict = {}
    for w1, w2 in zip(inputStr,inputStr[1:]):
        tmp=w1+w2
        if tmp.isalpha():
            if tmp in dict:
                dict[tmp] = dict[tmp] + 1
            else:
                dict[tmp] = 1
    return dict
    
def solution(str1, str2):
    answer = 0
    #초기 작업
    str1,str2 = str1.lower(), str2.lower() 
    
    #각 문자를 2개씩 끊는다.
    #문자가 아닌게 있다면 버린다.
    s1=getSet(str1)
    s2=getSet(str2)
    if len(s1)==0 and len(s2)==0:
        return 65536
    
    unionCount = union(s1,s2)
    intersectionCount = intersection(s1,s2)
    answer = int((intersectionCount/unionCount) * 65536)
    return answer