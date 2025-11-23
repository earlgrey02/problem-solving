import sys
from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())
chars = sorted(input().split())
vowels = set(('a', 'e', 'i', 'o', 'u'))

for password in combinations(chars, l):
    if (vowel_count := sum(1 for i in password if i in vowels)) >= 1 and l - vowel_count >= 2:
        print(''.join(password))