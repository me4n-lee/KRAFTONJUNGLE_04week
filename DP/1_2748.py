#https://www.acmicpc.net/problem/2748
#피보나치 수 2
#2748

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 91


def fun(n):

    if n == 0:
        dp[0] = 0
    if n == 1:
        dp[1] = 1

    if n >= 2:
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

    return dp


result = fun(n)
answer = result[n]

print(answer)