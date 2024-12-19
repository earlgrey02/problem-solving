from collections import Counter
import sys

input = sys.stdin.readline

word = input().strip().upper()
counter = Counter(word).most_common()

print(counter[0][0] if len(set(filter(lambda x: x[1] == counter[0][1], counter))) == 1 else '?')