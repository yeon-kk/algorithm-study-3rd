# 주유소

# 배열 길이가 달라서 복잡하게 생각할 수 있지만, index는 공유하는 문제
# 따라서, 배열 길이를 동일하게 맞춰준다.
# if-else문에 공통된 부분을 밖으로 빼주면 코드 길이를 줄일 수 있다.
# 설계 당시 코드
    # if localMin <= item:
    #     totalPrice+= localMin*road[pIdx]
    # else:
    #     localMin = price[pIdx]
    #     totalPrice += localMin * road[pIdx]
N=input()
road=list(map(int,input().split()))
prices=list(map(int,input().split()))

road.append(0)
totalPrice = 0
localMin = prices[0]
for pIdx, price in enumerate(prices):
    if localMin > price:
        localMin = price
    totalPrice += localMin * road[pIdx]
print(totalPrice)