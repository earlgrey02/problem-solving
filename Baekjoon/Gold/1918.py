import sys

input = sys.stdin.readline

expression = input().strip()
result, operators = [], []

for token in expression:
    if token.isalpha():
        result.append(token)
    else:
        if token == ')':
            while operators and operators[-1] != '(':
                result.append(operators.pop())

            operators.pop()
        else:
            if token in ('+', '-'):
                while operators and operators[-1] != '(':
                    result.append(operators.pop())
            elif token in ('*', '/'):
                while operators and operators[-1] in ('*', '/'):
                    result.append(operators.pop())

            operators.append(token)

result.extend(operators[::-1])

print(*result, sep = '')