import argparse
import networkx as nx
from collections import namedtuple

def read_input(composed_graph_file):
    with open(composed_graph_file) as fo:
        composed = fo.readlines()
    return composed

def read_graph(composed_graph_file):
    composed = read_input(composed_graph_file)

    State = namedtuple('State', 'tail head char1 char2 weight')

    states = []
    for line in composed[:-1]:
        line = line.split('\t')
        states.append(State(int(line[0]), int(line[1]), line[2], line[3], float(line[4])))

    G = nx.DiGraph()

    edges = [(s.tail, s.head, s.weight) for s in states]
    nodes = list(set([s.tail for s in states]))
    nodes.append(states[-1].head)

    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    return G, states

def main():
    if __name__=="__main__":

        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-c', '--composed', help='path to a file with composed transducer', required=True)
        parser.add_argument('-o', '--output', help='path to the output file', default='stdout')

        args = parser.parse_args()
        
        path = args.composed

        inp = read_input(path)

        G, states = read_graph(path)
        arbor = nx.minimum_spanning_arborescence(G, attr='weight')
        ## Print to att file states with matching sequences
        initial_edges =  [(s.tail, s.head) for s in states]
        att_graph = [states[initial_edges.index(e)] for e in arbor.edges if e in initial_edges]
        with open('example_min_spanning.txt', 'w') as fo:
            for s in att_graph:
                fo.write(str(s.tail)+'\t'+str(s.head)+'\t'+s.char1+'\t'+s.char2+'\t'+str(s.weight)+'\n')

main()

