def solution(string: str) -> bool:
    stack = []

    for parenthesis in string:
        if parenthesis == '(':
            stack.append(parenthesis)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    answer = not stack

    return answer