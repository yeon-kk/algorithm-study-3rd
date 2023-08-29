import sys
N,M = map(int,sys.stdin.readline().split())
homes = []
for _ in range(N):
    homes.append(list(map(int,sys.stdin.readline().split())))
K =int(sys.stdin.readline())
ranges = []
for _ in range(K):
    ranges.append(list(map(int,sys.stdin.readline().split())))
dp = [ [0]*(1+M) for _ in range(1+N)]
for row in range(N):
    for col in range(M):
        dp[row+1][col+1] = homes[row][col] + dp[row][col+1] + dp[row+1][col] - dp[row][col]
for y1,x1,y2,x2 in ranges:
    print(dp[y2][x2] - dp[y2][x1-1] - dp[y1-1][x2] + dp[y1-1][x1-1])

