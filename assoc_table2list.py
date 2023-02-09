removeTID = True
transactions = """
TID a b c d e f g h i j k l m n o p 
1 1 0 1 0 0 1 0 1 0 0 0 0 0 0 0 0
2 1 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0
3 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0
4 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0
5 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0
6 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0
7 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 0
8 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
9 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0
10 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0
11 1 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0
12 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0
13 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0
14 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0
15 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0
16 1 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0
17 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0
18 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0
19 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
20 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 1
""".split("\n")[1:-1]

if removeTID:
    transactions = list(map(lambda x: x.split()[1:], transactions))
else:
    transactions = list(map(lambda x: x.split(), transactions))
headers = transactions[0]
headerDict = {i: header for header, i in enumerate(headers)}
transactions = transactions[1:]
transactions = [list(map(int, transaction)) for transaction in transactions]

for transaction in transactions:
    [print(c,end='') for i, c in enumerate(headers) if transaction[i]==1]
    print()