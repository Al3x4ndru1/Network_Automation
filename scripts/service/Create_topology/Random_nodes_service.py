import random

def check(mat):
    nr_of_links = 0
    for j in mat:
        if j == 1:
            nr_of_links += 1
            if nr_of_links == 2:
                return True
    return False

def remake(mat, k, n):
    nr_of_links = 0
    if k == 0:
        for i in range(1, len(mat)):
            if mat[k][i] == 0 and i != k:
                mat[k][i] = random.randint(0, 1)
                mat[i][k] = mat[k][i]
            else:
                nr_of_links += 1
        return mat
    if k == n:
        for i in range(len(mat) - 1):
            if mat[k][i] == 0 and i != k:
                mat[k][i] = random.randint(0, 1)
                mat[i][k] = mat[k][i]
            else:
                nr_of_links += 1
        return mat

    for i in range(len(mat)):
        if mat[k][i] == 0 and i != k:
            mat[k][i] = random.randint(0, 1)
            mat[i][k] = mat[k][i]
        else:
            nr_of_links += 1

    if nr_of_links < 2:
        if not check(mat[k]):
            mat = remake(mat, k, n)

    return mat

def random_nodes_service(number_of_nodes, number_of_hosts_per_node):
    
    mat = [[0 for _ in range(number_of_nodes)] for _ in range(number_of_nodes)]

    for i in range(number_of_nodes):
        number_of_indices = 0
        for j in range(number_of_nodes):
            if i == j:
                mat[i][j] = 0
            else:
                if mat[i][j] == 0:
                    mat[i][j] = random.randint(0, 1)
                    mat[j][i] = mat[i][j]
                    if mat[j][i] == 1:
                        number_of_indices += 1
                    if j == number_of_nodes - 1 and number_of_indices < 2:
                        mat = remake(mat, i, number_of_nodes - 1)
                else:
                    number_of_indices += 1

    node_map = {}
    for i in range(number_of_nodes):
            
        node_map[i] = {}
        node_map[i]["switches_links"] = [j for j in range(number_of_nodes) if mat[i][j] != 0]
        node_map[i]["number_of_hosts"] = random.randint(1,number_of_hosts_per_node)

    return node_map