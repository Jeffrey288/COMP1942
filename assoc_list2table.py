import re
from string import ascii_uppercase

transactions = re.sub('[^A-Z\n]', '', """
1 Q, T
2 H, Q, T
3 S
4 H, Q, S, T
5 H, Q, S
""").split('\n')[1:-1]

freqDict = {}
for c in ascii_uppercase:
    freqDict[c] = 0
for transaction in transactions:
    for c in transaction:
        freqDict[c] += 1
freqItems = [c for c in ascii_uppercase if freqDict[c] > 0]
[print(c, end=' ') for c in freqItems]
print()
for transaction in transactions:
    [print(0 if c in transaction else 1, end=' ') for c in freqItems]
    print()