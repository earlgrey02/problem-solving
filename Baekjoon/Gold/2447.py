import sys

input = sys.stdin.readline

def draw_stars(n: int) -> list[str]:
    if n == 1:
        return ['*']
    else:
        stars = draw_stars(n // 3)
        extended_stars = []

        for star in stars:
            extended_stars.append(star * 3)

        for star in stars:
            extended_stars.append(star + ' ' * (n // 3) + star)

        for star in stars:
            extended_stars.append(star * 3)

        return extended_stars

n = int(input())

print(*draw_stars(n), sep = '\n')