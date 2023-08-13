import sys
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    n=int(sys.stdin.readline().rstrip())
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    if n>1:
        dp[2]=2
    if n>2:
        dp[3]=4
    for idx in range(4,n+1):
        dp[idx] = dp[idx-1] + dp[idx-2] + dp[idx-3]
    print(dp[-1])
    