import sys
input = sys.stdin.readline

a_list = list(input().strip())
b_list = list(input().strip())

a = len(a_list)
b = len(b_list)

dp = [[0] * (b+1) for _ in range(2)]

def fun():
    max_length = 0
    max_index = 0

    for i in range(1, a+1):
        for j in range(1, b+1):
            if a_list[i-1] == b_list[j-1]:
                dp[1][j] = dp[0][j-1] + 1
                if dp[1][j] > max_length:
                    max_length = dp[1][j]
                    max_index = i
            else:
                dp[1][j] = 0

        dp[0] = dp[1][:]
    
    print(dp)
    return max_length, max_index

length, index = fun()
answer = a_list[index - length:index]

print(length)
print(''.join(answer))
