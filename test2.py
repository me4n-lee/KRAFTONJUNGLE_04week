import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

dp = [[-1] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs_stack(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs_stack(nx, ny)

    return dp[x][y]

answer = dfs_stack(0, 0)
print(answer)


