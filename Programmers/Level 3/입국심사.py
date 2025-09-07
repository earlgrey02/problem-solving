def solution(n: int, times: list[int]) -> int:
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        count = sum(mid // time for time in times)

        if count < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

    return answer