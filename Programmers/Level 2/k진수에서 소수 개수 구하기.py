from math import isqrt

def solution(n, k):
    def format(n, k):
        formatted_n = []

        while n > 0:
            n, mod = divmod(n, k)
            formatted_n.append(str(mod))

        return ''.join(formatted_n[::-1])

    def is_prime(n):
        if n <= 1:
            return False

        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False

        return True

    numbers = [int(digit) for digit in format(n, k).split('0') if digit]
    answer = len([number for number in numbers if is_prime(number)])

    return answer