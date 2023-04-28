#https://www.acmicpc.net/problem/11049
#행렬 곱셈 순서
#11049

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a,b = map(int, input().split())
    graph.append([a,b])


dp = [[0] * (n) for _ in range(n)]

# print(graph)
# print(dp)

def fun(n, graph):

    for i in range(n):
        for j in range(n):

            if i == j:
                dp[i][j] = 0
            
            if i+1 == j:
                dp[i][j] = graph[i][0] * graph[i][1] * graph[j][1]

            else:
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + graph[i][0] * graph[k][1] * graph[j][1])

    return dp

result = fun(n, graph)
print(result[0][n-1])