from string import ascii_lowercase
import re
def addComma(items):
    return ''.join([(item+',') for item in items[:-1]]) + items[-1]

threshold = 2
transactions = re.sub('[^a-z\n]', '', """
1 b, d, f, r
2 b, c, d, s
3 c, m, t
4 b, d, f
5 a, d, f
6 e, f
7 f, h
8 b, d, c
9 a, l
10 c, g
11 c, k
12 f, n, o
13 b, c, d, p
14 f, j, q
15 c, i
16 a, d 
""").split('\n')[1:-1] # will only see alphabet
b_i = '\033[1m'
b_f = '\033[0m'

t1, t2, t3 = [], [], []

freqDict = {}
for c in ascii_lowercase:
    freqDict[c] = 0
for transaction in transactions:
    for c in transaction:
        freqDict[c] += 1

t1.append("Frequency Table")
t1.append(f"{'Items':<6}{'Freq.':<6}")
freqItems = []
for c in ascii_lowercase:
    if freqDict[c] > 0:
        t1.append(f"{c:^6}{freqDict[c]:^6}")
        if freqDict[c] >= threshold:
            freqItems.append([c, freqDict[c]])

freqItems = sorted(freqItems, key=lambda x: x[1], reverse=True)
t2.append(f"Frequent Tables")
t2.append(f"(Threshold = {threshold})")
t2.append(f"{'Items':<6}{'Freq.':<6}")
for freqItem, freq in freqItems:
    t2.append(f"{freqItem:^6}{freq:^6}")
freqItemsOrder = [item[0] for item in freqItems]

t3.append(f"Transactions")
t3.append(f"{'TID':<5}{'Items':<12}{'Sorted Freq. Items':<20}")
sortedTransactions = []
for i, items in enumerate(transactions):
    sorted_freq_items = ''.join([item for item in freqItemsOrder if item in items])
    t3.append(f"{i+1:<5}{addComma(items):<12}{addComma(sorted_freq_items):<20}")
    sortedTransactions.append(sorted_freq_items)

[print() for _ in range(2)]
for i in range(max([len(t1), len(t2), len(t3)])):
    l1 = t1[i] if i < len(t1) else ''
    l2 = t2[i] if i < len(t2) else ''
    l3 = t3[i] if i < len(t3) else ''
    print('{:<16} | {:<16} | {}'.format(l1, l2, l3))
[print() for _ in range(2)]

def freqTable(transactions):
    freqDict = {}
    for c in ascii_lowercase:
        freqDict[c] = 0
    for transaction in transactions:
        for c in transaction:
            freqDict[c] += 1
    freqItems = []
    for c in ascii_lowercase:
        if freqDict[c] > 0:
            freqItems.append([c, freqDict[c]])
    return freqDict, freqItems

def applyThresholdAndSort(freqDict):
    freqItems = []
    for c in ascii_lowercase:
        if freqDict[c] >= threshold:
            freqItems.append([c, freqDict[c]])
    freqItems = sorted(freqItems, key=lambda x: x[1], reverse=True)
    return freqItems

def editTransactions(transactions, freqItems):
    freqItemsOrder = [item[0] for item in freqItems]
    sortedTransactions = []
    for i, items in enumerate(transactions):
        sorted_freq_items = ''.join([item for item in freqItemsOrder if item in items])
        sortedTransactions.append(sorted_freq_items)
    return sortedTransactions


transaction_subset = []

for i,cond_fp_tree in enumerate(freqItemsOrder[::-1]):
    print(f'Conditional FP-Tree on {cond_fp_tree}:')
    transaction_subset = [transaction[::-1] for transaction in sortedTransactions if cond_fp_tree in transaction]
    transaction_subset = ["".join([letter for letter in transaction if letter in freqItemsOrder[::-1][i:]]) for transaction in transaction_subset]
    print("1. transactions:", transaction_subset)
    cond_freqDict, cond_itemCount = freqTable(transaction_subset)
    print("2. frequencies:", cond_itemCount)
    cond_freqCount = applyThresholdAndSort(cond_freqDict)
    print("3. frequencies (w/ threshold):", cond_freqCount)
    ordered_transaction_subset = editTransactions(transaction_subset, cond_freqCount)
    print("4. ordered transactions:", ordered_transaction_subset)
    print(f'5. count = {cond_freqDict[cond_fp_tree]}')
    print()
    # applyThresholdAndSort
