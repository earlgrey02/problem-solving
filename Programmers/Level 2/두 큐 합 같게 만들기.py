def solution(queue1, queue2):
    numbers = queue1 + queue2
    answer = -1

    if sum(numbers) % 2 == 0:
        target = sum(numbers) // 2
        summation = sum(queue1)
        left, right = 0, len(queue1) - 1
        count = 0

        while right < len(numbers) - 1:
            if summation < target:
                right += 1
                summation += numbers[right]
                count += 1
            elif summation > target:
                summation -= numbers[left]
                left += 1
                count += 1
            else:
                answer = count
                break

    return answer