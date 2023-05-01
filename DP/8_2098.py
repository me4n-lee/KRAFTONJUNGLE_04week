#https://www.acmicpc.net/problem/2098
#외판원 순회
#2098

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

print(graph)

visit = [[0] * n for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def fun(first):

    stack = []
    stack.append(first)

    while stack:

        start, end = stack.pop()

        for i in range(4):
            n_start = start + dx
            n_end = end + dy

fun((0,0))