import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_color(G,i):
    ###
    smallest_colour = 1

    neighbours = [(_, G.node[_]['color']) for _ in G[i] if not G.node[_]['color'] == 'never coloured']
    neighbours.sort(key= lambda x: x[1])
    for n in neighbours:
        if not n[1] == 'never coloured':
            if n[1] == smallest_colour:
                smallest_colour = n[1] + 1

    G.node[i]['color'] = smallest_colour
    return G
    ###

def greedy(G):
    #### 
    n = len(G.nodes())
    for i in range(1, n+1):
        G = find_smallest_color(G, i)
    kmax = max([G.node[_]['color'] for _ in G.nodes()])
    ####
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)