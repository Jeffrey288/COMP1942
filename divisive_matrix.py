import numpy as np

SINGLE, COMPLETE, GROUPAVG = 0, 1, 2
mode = GROUPAVG
# ! DO NOT USE CENTROID OR MEDIAN
dist_matrix = """
0
10 0
7 7 0
30 23 21 0
29 25 22 7 0
38 34 31 10 11 0
42 36 36 13 17 9 0
""".split('\n')[1:-1]
# ---------------------------------
dist_matrix = list(map(lambda x: list(map(float, x.split())), dist_matrix))
pt_count = len(dist_matrix[-1])
dist_matrix = [[(dist_matrix[i][j] if i >= j else dist_matrix[j][i]) for i in range(pt_count)] for j in range(pt_count)]
cluster1 = []
cluster2 = [i for i in range(pt_count)]
 
SingleLinkage = lambda pt, cluster: min([dist_matrix[pt][i] for i in cluster])
CompleteLinkage = lambda pt, cluster: max([dist_matrix[pt][i] for i in cluster])
GroupAverageLinkage = lambda pt, cluster: sum([dist_matrix[pt][i] for i in cluster])/len(cluster)
def Linkage(pt, cluster):
    def cleanCluster(pt, cluster):
        return [i for i in cluster if i != pt]
    cleanedCluster = cleanCluster(pt, cluster)
    
    if mode == SINGLE:
        return SingleLinkage(pt, cleanedCluster)
    elif mode == COMPLETE:
        return CompleteLinkage(pt, cleanedCluster)
    elif mode == GROUPAVG:
        return GroupAverageLinkage(pt, cleanedCluster)


def displayPoints(pts):
    return list(map(lambda x: x+1, pts))
def displayDistances(displayType, pts, distances):
    format_string = ''.join([("{:<20}\n" if (i%4==3 and i!=len(pts)-1) else "{:<20}") for i in range(len(pts))])
    f_pts = displayPoints(pts)
    string_list = [
            {
                '*': f'D({pt}, *) = {distance:.2f}',
                'A': f'D({pt}, A) = {distance:.2f}',
                'B': f'D({pt}, B) = {distance:.2f}',
                'd': f'Δ{pt} = {distance:.2f}'
            }[displayType]
         for pt, distance in zip(f_pts, distances)]
    return format_string.format(*string_list)

dists = [Linkage(i, cluster2) for i in cluster2]
[print() for _ in range(2)]
print(displayDistances('*', cluster2, dists))
index = dists.index(max(dists))
cluster2.remove(index)
cluster1.append(index)
print(f"Since point {index+1} has the maximum distance from cluster B, we will move it to cluster A.")
print(f'A: {displayPoints(cluster1)},     B: {displayPoints(cluster2)}.')
while True:
    [print() for _ in range(2)]
    dists2 = [Linkage(i, cluster2) for i in cluster2]
    dists1 = [Linkage(i, cluster1) for i in cluster2]
    dists = [dists2[i] - dists1[i] for i in range(len(cluster2))]
    print(displayDistances('B', cluster2, dists2))
    print(displayDistances('A', cluster2, dists1))
    print(displayDistances('d', cluster2, dists))
    if max(dists) < 0:
        break
    index = cluster2[dists.index(max(dists))]
    cluster2.remove(index)
    cluster1.append(index)
    print(f"Since point {index+1} is farthest from cluster B, we will move it to cluster A.")
    print(f'A: {displayPoints(cluster1)},     B: {displayPoints(cluster2)}.')
print(f'Since all of the deltas are negative (i.e. closer to cluster B than cluster A), the algorithm stops here.')
print(f'Final clusters: A: {displayPoints(cluster1)},     B: {displayPoints(cluster2)}.')
[print() for _ in range(2)]
ClusterSingleLinkage = lambda cluster1, cluster2: min([dist_matrix[j][i] for i in cluster1 for j in cluster2])
ClusterCompleteLinkage = lambda cluster1, cluster2: max([dist_matrix[j][i] for i in cluster1 for j in cluster2])
ClusterGroupAverageLinkage = lambda cluster1, cluster2: sum([dist_matrix[j][i] for i in cluster1 for j in cluster2])/len(cluster1)/len(cluster2)
if mode == SINGLE:
    print('Distance between two clusters:', ClusterSingleLinkage(cluster1, cluster2))
elif mode == COMPLETE:
    print('Distance between two clusters:', ClusterCompleteLinkage(cluster1, cluster2))
elif mode == GROUPAVG:
    print('Distance between two clusters:', ClusterGroupAverageLinkage(cluster1, cluster2))

[print() for _ in range(2)]