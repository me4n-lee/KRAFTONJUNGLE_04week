#https://www.acmicpc.net/problem/9249
#최장 공통 부분 문자열
#9249

import sys
input = sys.stdin.readline

a_list = list(input().strip())
b_list = list(input().strip())

print(a_list)
print(b_list)

a = len(a_list)
b = len(b_list)

#first 를 second 로 확인
#세로 가로를 확실하게 체크하지 않으면 인덱스 에러 발생
dp = [[0] * (b+1) for _ in range(a+1)]

# print(dp)

new_list = []

def fun():
    for i in range(1, a+1):
        for j in range(1, b+1):
            
            # if first_list[i] == 0 or second_list[j] == 0:
            #     continue

            if a_list[i-1] == b_list[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp


result = fun()
print(result)
answer = result[a][b]
print(answer)