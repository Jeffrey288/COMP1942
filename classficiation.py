import math

ID3, C45, CART = 0, 1, 2 # ! <--------- the modes u can choose from
mode = C45 # ! <---------- change to ID3, C45 or CART depending on what u use
YES, NO = "yes", "no" 
# YES, NO = "1", "0"
first_row_id = True # ! <------- if the first row is No. the put True, else False
records = """
No. Income Gender Education Study_PhD
1 low female bachelor yes
2 medium female bachelor yes
3 high male bachelor yes
6 high male bachelor no
""".split('\n')[1:-1]
records = list(map(lambda x: x.split(), records))
header = records[0]
records = records[1:]
if first_row_id:
    header = header[1:]
    records = [record[1:] for record in records]
# write(records)

f = open("classification.txt", "w")
sqrtsym = "^2"
# sqrtsym = "²"

def write(*args,):
    global f
    print(*args,)
    f.write("".join([arg.__str__()+" " for arg in args])[:-1]+'\n')

attr_count = len(header) - 1
record_count = len(records)

def info(pList):
    if mode == ID3 or mode == C45:
        total = 0
        for p in pList:
            if p == 0:
                total += 0
            elif p == 'undef':
                total += 0
            else:
                total += -1*p*math.log2(p)
        return total
    elif mode == CART:
        total = 1
        for p in pList:
            if p == 'undef':
                pass
            else:
                total -= p**2
        return total

write()
write(f"Impurity measurement used:", 
    "ID3" if mode == ID3 else "C4.5" if mode == C45 else "CART" if mode == CART else "undefined"
    ,".")
write()
record_lookup = [record[attr_count] for record in records]
n_T_yes = record_lookup.count(YES)
n_T_no = record_lookup.count(NO)
p_T_yes = n_T_yes / record_count
p_T_no = n_T_no / record_count
T_Info = info([p_T_no, p_T_yes])
if mode == CART:
    write(f"Info(T) = 1 - ({n_T_yes}/{record_count}){sqrtsym} - ({n_T_no}/{record_count}){sqrtsym} = {T_Info:.4f}")
else:
    write(f"Info(T) = -({n_T_yes}/{record_count})log({n_T_yes}/{record_count})-({n_T_no}/{record_count})log({n_T_no}/{record_count}) = {T_Info:.4f}")
write()
for i, attr in enumerate(header[:-1]):
    write(f"For the attribute {attr},")
    record_list = [record[i] for record in records]
    values = set(record_list)
    value_n = []
    value_Info = []
    for value in sorted(list(values)):
        index_list = [i for i in range(record_count) if record_list[i] == value]
        index_lookup = [record_lookup[i] for i in index_list]
        n_yes = index_lookup.count(YES)
        n_no = index_lookup.count(NO)
        n = len(index_list)
        p_yes = n_yes / n
        p_no = n_no / n
        Info = info([p_yes, p_no])
        if mode == CART:
            write(f"Info(T_{value}) = 1 - ({n_yes}/{n}){sqrtsym} - ({n_no}/{n}){sqrtsym} = {Info:.4f}")
        else:
            write(f"Info(T_{value}) = -({n_yes}/{n})log({n_yes}/{n})-({n_no}/{n})log({n_no}/{n}) = {Info:.4f}")
        value_n.append(n)
        value_Info.append(Info)
    TotalInfo = sum([n*Info for n, Info in zip(value_n, value_Info)])/record_count
    write(f"Info({attr}, T) = " + "".join([f" ({n}/{record_count})*{Info:.4f} +" for n, Info in zip(value_n, value_Info)])[:-2] \
                           + f" = {sum([n*Info for n, Info in zip(value_n, value_Info)])/record_count:.4f}")
    if mode == C45:
        SplitInfo = info([record_list.count(value)/record_count for value in values])
        write(f"SplitInfo({attr}) = " + "".join([f" [-({record_list.count(value)}/{record_count})log({record_list.count(value)}/{record_count})] +" for value in values])[:-2] \
                        + f" = {SplitInfo:.4f}")
        if SplitInfo != 0:
            write(f"Gain({attr}, T) = ({T_Info:.4f} - {TotalInfo:.4f}) / {SplitInfo:.4f} = {(T_Info-TotalInfo)/SplitInfo:.4f}")
        else:
            write("SplitInfo is 0.")
    else:
        write(f"Gain({attr}, T) = {T_Info:.4f} - {TotalInfo:.4f} = {(T_Info-TotalInfo):.4f}")
    write()


