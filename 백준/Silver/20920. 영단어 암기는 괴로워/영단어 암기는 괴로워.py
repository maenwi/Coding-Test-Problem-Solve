import sys
input = sys.stdin.readline

from collections import Counter

N, M = map(int, input().split())

words = {}
for _ in range(N):
    word = input().strip()

    if len(word) < M:
        continue

    try:
        words[word][0] += 1
    except:
        words[word] = [1, len(word)]

sorted_words = sorted(words.items(), key=lambda item: (-item[1][0], -item[1][1], item[0]))

for k, _ in sorted_words:
    print(k)
