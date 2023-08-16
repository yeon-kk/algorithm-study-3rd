n=int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 1
if n != 0:
    dp[1] = 1
    for num in range(2,n+1):
        for k in range(num):
            dp[num] += (dp[k]*dp[num-1-k])
print(dp[-1])