import networkx as nx
import matplotlib.pyplot as plt

def Graph():
    # Diameter = 2*arm_len + 1
    # kmax = 2
    # DFS: should visit (if b=9) all nodes, reaching b last with path = 2 (a=1)
    # BFS: a=1, b= 5, path = 2  

    nb_arms = 2
    arm_len = 200

    G = nx.Graph()

    for i in range(1, nb_arms*arm_len + 2):
        G.add_node(i)

    for i in range(2, nb_arms*arm_len + 1, arm_len):
        G.add_edge(1, i)
        for a in range(1, arm_len):
            G.add_edge(i+a - 1, i+a)
    
    return G

G = Graph()
nx.draw_networkx(G)
plt.show()