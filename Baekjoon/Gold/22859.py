import sys
from re import sub

input = sys.stdin.readline

html = input().strip()

html = sub(r"</?main>", '', html)
html = sub(r"<div title=\"(.*?)\">", r"title : \1\n", html)
html = sub(r"</div>", '', html)
html = sub(r"<p>(.*?)</p>", r"\1\n", html)
html = sub(r"<(.*?)/?>", '', html)
html = sub(r" {2,}", ' ', html)

print(html)