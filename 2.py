#https://www.acmicpc.net/problem/1520
#내리막 길
#1520

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

dp = [[-1] * (m+1) for _ in range(n+1)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
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
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


answer = dfs(0, 0)
print(dp)
print(answer)
