import networkx as nx
import matplotlib.pyplot as plt

def Graph():
    # Diameter = n
    # kmax = 2
    # DFS = Should traverse in order until b reached
    # BFS = 
    G = nx.hypercube_graph(3)

    return G

G = Graph()
print(nx.diameter(G))
nx.draw_networkx(G)
plt.show()