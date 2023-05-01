#https://www.acmicpc.net/problem/1541
#잃어버린 괄호
#1541

import sys
input = sys.stdin.readline

n_list = list(map(str, input().strip().split('-')))

# print(n_list)


def fun(n_list):

    result = 0

    for i in range(len(n_list)):
        plus_result = 0
        plus_list = []

        plus_list = n_list[i].split('+')
        # print(plus_list)

        for j in range(len(plus_list)):
            plus_result += int(plus_list[j])
        
        # print(plus_result)

        if i == 0:
            result += plus_result

        else:
            result -= plus_result

    return result


answer = fun(n_list)
print(answer)