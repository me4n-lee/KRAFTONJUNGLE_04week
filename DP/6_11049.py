#https://www.acmicpc.net/problem/11049
#행렬 곱셈 순서
#11049

import sys

n = int(input())

graph = []
for _ in range(n):
    a, b = map(int, input().split())
    graph.append([a, b])

dp = [[0] * n for _ in range(n)]

for length in range(1, n):  # 행렬 곱셈 길이
    for i in range(n - length):  # 시작 행렬 인덱스
        j = i + length  # 끝 행렬 인덱스
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + graph[i][0] * graph[k][1] * graph[j][1])

print(dp[0][n-1])