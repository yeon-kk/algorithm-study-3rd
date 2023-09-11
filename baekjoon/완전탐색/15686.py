import sys
N,M= map(int,sys.stdin.readline().split())
arr =[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

homes = []
chickens = []

for row in range(N):
    for col in range(N):
        if arr[row][col]==1:
            homes.append((row,col))
        elif arr[row][col]==2:
            chickens.append((row,col))
min_distance = int(1e9)
homes_length = len(homes)
chickens_length = len(chickens)
distances = [[] for _ in range(homes_length)]
for idx, home in enumerate(homes):
    hy, hx = home
    for  chicken in  chickens:
        cy, cx = chicken
        distances[idx].append(abs(hy-cy)+abs(hx-cx))

results = []

def backtracking(idx):
    global distances, min_distance, results, M, chickens_length
    if len(results)==M:
        tmp = 0
        for dists in zip(*results):
            tmp += min(dists)
        min_distance = min(min_distance,tmp)
        return
    for i in range(idx,chickens_length): #dist col
        tmp = []
        for j in range(homes_length):
            cost=distances[j][i]
            tmp.append(cost)
        results.append(tmp)
        backtracking(i+1)
        results.pop()
for idx in range(chickens_length):
    backtracking(idx)
print(min_distance)