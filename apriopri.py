
import enum

threshold = 2
removeTID = False
transactions = """
h q s t
0 1 0 1
1 1 0 1
0 0 1 0
1 1 1 1
1 1 1 0
""".split("\n")[1:-1]

# antecedent, consequent = '',''
antecedent, consequent = '',''


if removeTID:
    transactions = list(map(lambda x: x.split()[1:], transactions))
else:
    transactions = list(map(lambda x: x.split(), transactions))
headers = transactions[0]
headerDict = {i: header for header, i in enumerate(headers)}
transactions = transactions[1:]
transactions = [list(map(int, transaction)) for transaction in transactions]

attr_count = len(headers)
transactions_count = len(transactions)

def support(itemset):
    return len([1 for transaction in transactions if sum([transaction[headerDict[item]] for item in itemset])==len(itemset)])

b_i = '\033[1m'
b_f = '\033[0m'
print()
if antecedent != '' and consequent != '':
    ant_set = '{'+''.join([i+',' for i in antecedent])[:-1]+'}'
    con_set = '{'+''.join([i+',' for i in consequent])[:-1]+'}'
    rule = f'{ant_set}->{con_set}'
    print(b_i+'Parameters'+b_f)
    print(f'For the association rule {rule},')
    print(f'supp({rule}) = {support(antecedent+consequent)}')
    print(f'conf({rule}) = supp({rule})/supp({ant_set}) = '+\
        f'{support(antecedent+consequent)}/{support(antecedent)} = '+\
        f'{support(antecedent+consequent)/support(antecedent):.2f}')
    print(f'expconf({con_set}) = supp({con_set})/N = '+\
        f'{support(consequent)}/{transactions_count} = '
        f'{support(consequent)/transactions_count:.2f}')
    print(f'lift({rule}) = conf({rule})/expconf({con_set}) = '+\
        f'({support(antecedent+consequent)}/{support(antecedent)})/({support(consequent)}/{transactions_count}) = '+\
        f'{(support(antecedent+consequent)/support(antecedent))/(support(consequent)/transactions_count):.2f}')


print()
print(b_i+'Apriori Algorithm'+b_f)
L = {}
C = {}
L[1] = [header for header in headers if support(header)>threshold]
print('\033[92m'+'L1:', [f'{itemset}: {support(itemset)}' for itemset in L[1]], '\033[0m')
itemset_size = 2
while len(L[itemset_size-1]) > 0:
    C[itemset_size] = [
                L[itemset_size-1][i]+L[itemset_size-1][j][-1] 
                for i in range(len(L[itemset_size-1])) for j in range(len(range(len(L[itemset_size-1])))) 
                if (i<j and i!=j and L[itemset_size-1][i][:-1]==L[itemset_size-1][j][:-1])
            ]
    print(f'Joined C{itemset_size}:', C[itemset_size])
    if C[itemset_size] == []:
        print(f'C{itemset_size} is empty. Apriori Algorithm stops here.')
        break
    C[itemset_size] = [itemset for itemset in C[itemset_size] if 
        sum([(0 if subset in L[itemset_size-1] else 1) for subset in 
            [''.join([item for item in itemset if item!=exclude]) for exclude in itemset]]) == 0]
    print(f'Pruned C{itemset_size}:', C[itemset_size])
    print(f'C{itemset_size} Counts:', [f'{itemset}: {support(itemset)}' for itemset in C[itemset_size]])
    L[itemset_size] = [itemset for itemset in C[itemset_size] if support(itemset)>=threshold]
    print('\033[92m'+f'L{itemset_size}:', [f'{itemset}: {support(itemset)}' for itemset in L[itemset_size]],'\033[0m')
    itemset_size += 1

LAll = []
for i in range(1, itemset_size):
    LAll += L[i]
print('\033[92m'+f'Generated Large Itemsets (threshold = {threshold}):\n{LAll}','\033[0m')
print()