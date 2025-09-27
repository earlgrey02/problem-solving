def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start, end = 1, distance

    while start <= end:
        mid = (start + end) // 2
        count = 0
        prev = 0

        for rock in rocks:
            if rock - prev < mid:
                count += 1
            else:
                prev = rock

        if count <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer