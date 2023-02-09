from dis import dis
import math

# NO HEADER!
records = """
1 4 3 No
2 3 2 Yes
3 4 9 No
4 9 1 Yes
5 10 4 Yes
6 6 2 No
7 8 3 Yes
8 1 9 Yes
9 2 10 Yes
10 4 8 No
11 6 7 No
12 8 6 Yes
13 7 5 No
14 5 6 No 
""".split('\n')[1:-1]
newRecord = "7 7"
recordID = True
k = 3

if recordID:
    records = [record.split()[1:] for record in records]
    newRecord = newRecord.split()
else:
    records = [record.split() for record in records]
    newRecord = newRecord.split()
records_attr = [list(map(float, record[:-1])) for record in records]
records_target = [record[-1] for record in records]
newRecord = list(map(float, newRecord))
attrCount = len(records_attr[0])
# check
if (len(newRecord) != attrCount):
    raise Exception(f"new record has wrong no. of attributes! expected {attrCount} got {len(newRecord)}")

def EuclideanDistance(t1, t2):
    return math.sqrt(sum((e1-e2)**2 for e1, e2 in zip(t1, t2)))
dists = [EuclideanDistance(record, newRecord) for record in records_attr]
sorted_dist_tuples = sorted([(ind+1, dist) for ind, dist in enumerate(dists)], key=lambda x: x[1])
min_dist_indices = [tup[0] for tup in sorted_dist_tuples][:k]
print("Distances from new record:", dists)
print("Sorted (recordID, distances) tuples:", sorted_dist_tuples)
print("Nearest k neighbours:", min_dist_indices)
print("Target attributes of nearest neighbours:", [records_target[ind-1] for ind in min_dist_indices])
