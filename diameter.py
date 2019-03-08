import networkx as nx
import random as rd
import graph6
import graph7
import graph8
import graph9
import graph10

def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.node[a]['label'] = 0

    ###
    i = 0
    while G.node[b]['label'] == -1:
        u_list = [_ for _ in G.nodes() if G.node[_]['label'] == i]
        for u in u_list:
            neighbours = [_ for _ in G[u] if G.node[_]['label'] == -1]
            for v in neighbours:
                G.node[v]['label'] = i+1

        i += 1
    return G.node[b]['label']    

def max_distance(G):
# Use breadth first search over every combination of nodes.
# Additionally, use in built functions to check correctness of my solutions.
# or, if feeling cheeky, use inbuilt nx.diameter(G)
    d = 0
    for s_n in G.nodes():
        c_n = [_ for _ in G.nodes()]# if not _ == s_n]
        for e_n in c_n:
            c = bfs(G, s_n, e_n)
            if c > d:
                d = c
    
    return d


print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()


G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()


G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()
