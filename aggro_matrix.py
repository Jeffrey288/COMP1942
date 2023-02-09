import math
SINGLE, COMPLETE, GROUPAVG = 0, 1, 2

# ---------------------

mode = GROUPAVG
# ! DO NOT USE CENTROID OR MEDIAN
dist_matrix = """

""".split('\n')[1:-1]

# ---------------------------------
dist_matrix = list(map(lambda x: list(map(float, x.split())), dist_matrix))
pt_count = len(dist_matrix[-1])
dist_matrix = [[(dist_matrix[i][j] if i >= j else dist_matrix[j][i]) for i in range(pt_count)] for j in range(pt_count)]


def distance(pt1, pt2):
    return dist_matrix[pt1][pt2]
class Cluster:
    def __init__(self, pt=None):
        if pt is None:
            self.pts_index = None
        else:
            self.pts_index = [pt]
    @staticmethod
    def merge(clus1, clus2):
        clus = Cluster()
        clus.pts_index = clus1.pts_index + clus2.pts_index
        return clus
    @staticmethod
    def dist(clus1, clus2):
        if clus1 == clus2:
            return 0
        pairwise_distances = [distance(i, j) for i in clus1.pts_index for j in clus2.pts_index]
        if mode == SINGLE:
            return min(pairwise_distances)
        elif mode == COMPLETE:
            return max(pairwise_distances)
        elif mode == GROUPAVG:
            return sum(pairwise_distances)/len(pairwise_distances)
        
def aggro(clusters):
    distance_matrix = [[Cluster.dist(i, j) for j in clusters] for i in clusters]
    min_dist, clus1_index, clus2_index = float('inf'), -1, -1
    for i in range(len(clusters)):
        for j in range(len(clusters)):
            if 0.00001 < distance_matrix[i][j] < min_dist:
                min_dist, clus1_index, clus2_index = distance_matrix[i][j], i, j
    return distance_matrix, min_dist, clus1_index, clus2_index

def display_points(pts):
    return str(list(map(lambda x: x+1, pts)))

def display_matrix(distance_matrix, clusters):
    cluster_labels = [display_points(clus.pts_index) for clus in clusters]
    print(("{:>12}"*(len(clusters)+1)).format("", *cluster_labels))
    for label, row in zip(cluster_labels, distance_matrix):
        print(("{:>12}"+"{:>12.1f}"*len(clusters)).format(label, *row))

def display_cluster(cluster):
    print(cluster.pts_index)


clusters = [Cluster(i) for i in range(pt_count)]

b_i = '\033[1m'
b_f = '\033[0m'
distance_matrix, min_dist, clus1_index, clus2_index = aggro(clusters)
print(b_i+"Initial Distance Matrix"+b_f)
# display_matrix(distance_matrix, clusters)

for _ in range(pt_count-1):
    distance_matrix, min_dist, clus1_index, clus2_index = aggro(clusters)
    display_matrix(distance_matrix, clusters)
    # [display_cluster(cluster) for cluster in clusters]
    print(b_i+f'The minimum distance is {min_dist:.4f} between clusters ' + \
              f'{display_points(clusters[clus1_index].pts_index)} and {display_points(clusters[clus2_index].pts_index)}.'+b_f)
    new_clus = Cluster.merge(clusters[clus1_index], clusters[clus2_index])
    print(b_i+f'The merged cluster is {display_points(new_clus.pts_index)}.'+b_f)
    clusters = [clusters[i] for i in range(len(clusters)) if i not in (clus1_index, clus2_index)] + [new_clus]
    # display_cluster(new_clus)
    # [display_cluster(cluster) for cluster in clusters]

