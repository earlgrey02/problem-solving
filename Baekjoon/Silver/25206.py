import sys

input = sys.stdin.readline

grade_points = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0
}
major_sum = 0
score_sum = 0

for _ in range(20):
    _, score, grade = input().split()

    if grade != "P":
        major_sum += float(score) * grade_points[grade]
        score_sum += float(score)

print(major_sum / score_sum)