from collections import Counter

text = input()

c = Counter(sorted(text.split()))

print(*sorted(c.keys(), key=c.get, reverse=True), sep='\n')