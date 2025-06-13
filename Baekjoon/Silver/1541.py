import sys

input = sys.stdin.readline

expressions = input().split('-')
answer = sum(map(int, expressions[0].split('+')))

for expression in expressions[1:]:
    answer -= sum(map(int, expression.split('+')))

print(answer)