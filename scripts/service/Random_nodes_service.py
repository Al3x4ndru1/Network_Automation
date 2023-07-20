import random
from pprint import PrettyPrinter


pp = PrettyPrinter(indent=2)

def check(mat):
    return mat.count(1) >= 2

def remake(mat, k, n):
    while mat[k].count(1) < 2:
        for i in range(n):
            if mat[k][i] == 0 and i != k:
                mat[k][i] = random.choice([0, 1])
                mat[i][k] = mat[k][i]
    return mat

def random_nodes_service(number_of_nodes):

    mat = [[0 if i == j else random.choice([0, 1]) for j in range(number_of_nodes)] for i in range(number_of_nodes)]

    for i in range(number_of_nodes):
        if mat[i].count(1) < 2:
            mat = remake(mat, i, number_of_nodes - 1)
            
            
    pp.pprint(mat)

    node_map = {}
    for i in range(number_of_nodes):
        node_map[i] = [j for j in range(number_of_nodes) if mat[i][j] != 0]

    return node_map