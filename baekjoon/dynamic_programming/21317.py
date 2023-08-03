# 큰 점프는 언제하지?
# 모든 경우에서 최소를 고려하기 어렵기 때문에, 인덱스 순으로 전부 K점프를 시행한 후 dp값을 구한다
N=int(input())
arr= [[0,0]]
dp = [0 for _ in range(N+1)]
for i in range(N-1):
    arr.append(list(map(int,input().split())))
K = int(input())
result = int(1e9)
dp[1]= 0
if N>1:
    dp[2]= dp[1] + arr[1][0]
if N>2:
    dp[3] = min(dp[1] + arr[1][1], dp[2] + arr[2][0])
if N>3:
    for jumpIdx in range(4,N+1):
        for idx in range(4,N+1):
            if idx==jumpIdx:
                dp[idx] = min(dp[idx-2] + arr[idx-2][1],dp[idx-1] + arr[idx-1][0],dp[idx-3]+K)
            else:
                dp[idx] = min(dp[idx - 2] + arr[idx - 2][1], dp[idx - 1] + arr[idx - 1][0])
        result = min(result,dp[-1])
if N<4:
    print(dp[-1])
else:
    print(result)