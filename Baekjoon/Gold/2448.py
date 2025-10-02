import sys

input = sys.stdin.readline

def draw_stars(n: int) -> list[str]:
    if n == 3:
        stars =  ["  *  ", " * * ", "*****"]
    else:
        before_stars = draw_stars(n // 2)
        stars = []

        for star in before_stars:
            stars.append(' ' * (n // 2) + star + ' ' * (n // 2))

        for star in before_stars:
            stars.append(star + ' ' + star)

    return stars

n = int(input())

print(*draw_stars(n), sep = '\n')