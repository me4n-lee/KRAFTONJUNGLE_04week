import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

dp = [[-1] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

stack = deque([(0, 0)])
dp[0][0] = 1

while stack:
    x, y = stack.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] < graph[x][y]:
            if dp[nx][ny] == -1:
                dp[nx][ny] = 0
                stack.append((nx, ny))
            dp[nx][ny] += dp[x][y]

answer = dp[n-1][m-1]
print(answer)
