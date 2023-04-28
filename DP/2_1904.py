#https://www.acmicpc.net/problem/1904
#01타일
#1904

import sys
input = sys.stdin.readline


n = int(input())
dp = [0] * 1000001


def fun(n):
    if n == 1:
        dp[1] = 1
    if n == 2:
        dp[2] = 2

    if n >= 3:
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746

    return dp

result = fun(n)
answer = result[n]
print(answer)