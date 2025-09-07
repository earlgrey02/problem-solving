def solution(numbers: list[int], target: int) -> int:
    def dfs(v: int, depth: int = 0):
        if depth == len(numbers):
            if v == target:
                nonlocal answer
                answer += 1
        else:
            dfs(v + numbers[depth], depth + 1)
            dfs(v - numbers[depth], depth + 1)

    answer = 0

    dfs(0)

    return answer