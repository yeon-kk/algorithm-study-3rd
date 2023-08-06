import sys
K,P,N=map(int, sys.stdin.readline().rstrip().split())

for _ in range(N):
    K = (K*P)%1000000007
print(K)