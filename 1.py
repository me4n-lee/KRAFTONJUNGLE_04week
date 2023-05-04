#https://www.acmicpc.net/problem/1890
#점프
#1890

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

dp = [[0] * n for _ in range(n)]

def fun():

    dp[0][0] = 1
    
    for i in range(n):
        for j in range(n):
            jump = graph[i][j]

            if i == n - 1 and j == n - 1:
                break

            if i + jump < n:
                dp[i+jump][j] += dp[i][j]
            
            if j + jump < n:
                dp[i][j+jump] += dp[i][j]

    return dp

result = fun()
# print(result)
answer = result[n-1][n-1]
print(answer)