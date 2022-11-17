vertex =    ['A',      'B',     'C',      'D',   'E',   'F',    'G']
weight = [  [  None,    29,    None,     None,  None,    10,  None ],
            [  29,    None,      16,     None,  None,  None,    15 ],
            [  None,    16,    None,       12,  None,  None,  None ],
            [  None,  None,      12,     None,    22,  None,    18 ],
            [  None,  None,    None,       22,  None,    27,    25 ],
            [  10,    None,    None,     None,    27,  None,  None ],
            [  None,    15,    None,       18,    25,  None,  None ] ]

parent = []
set_size = 0

def init_set(nSets) :
    global set_size, parent
    set_size = nSets
    for i in range(nSets) :
        parent.append(-1)
def find(id) :
    while (parent[id] >= 0):
        id = parent[id]
    return id
def union(s1, s2) :
    global set_size 
    parent[s1] = s2
    set_size = set_size -1
def set_clear() :
    global parent
    parent.clear()


def MaxSTKruskal(vertex, adj, mode) :
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    for i in range(vsize) :
        for j in range( i + 1 , vsize ) :
            if adj[i][j] != None :
                eList.append( (i, j, adj[i][j]))


    eList.sort(key = lambda e : e[2], reverse = True)

    edgeAccepted = 0
    v_sz = vsize -1
    result = 0

    while edgeAccepted <  v_sz :
        #if len(eList) == 0 : break

        if mode : e = eList.pop(-1)
        else : e = eList.pop(0)
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset :
            print("간선 추가 : {} - {} (비용:{})".format(vertex[e[0]], vertex[e[1]], e[2]))
            result += e[2]
            union(uset, vset)
            edgeAccepted += 1
    set_clear()
    return result


print("Kruskal's Algorithm")
print("MinST 가중치의 합 = ", MaxSTKruskal(vertex, weight, True))
print("MaxST 가중치의 합 = ", MaxSTKruskal(vertex, weight, False))
