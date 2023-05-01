#https://www.acmicpc.net/problem/11053
#가장 긴 증가하는 부분 수열
#11053

import sys
input = sys.stdin.readline

n = int(input())

a_list = list(map(int,input().split()))

# print(a_list)

dp = [1] * (n+1)

def fun():
    for i in range(n):
        for j in range(i):

            if a_list[i] > a_list[j]:
                # new_dp = dp[j] + 1
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

result = fun()
# print(result)
print(max(result))