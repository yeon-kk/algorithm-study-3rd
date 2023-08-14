import sys
n=int(sys.stdin.readline())
arr=[0]
arr+=list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]
dp[1] = arr[1]
for i in range(2,n+1):
    dp[i] = max(arr[i],dp[i-1]+arr[i])
print(max(dp[1:]))