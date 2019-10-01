import argparse
import networkx as nx

def read_graph(composed_graph_file):
    with open(composed_graph_file) as fo:
        composed = fo.readlines()

    G = nx.DiGraph()

    edges = [(int(line.split('\t')[0]), int(line.split('\t')[1]), float(line.split('\t')[-1].strip()))\
            for line in composed[:-1]]
    nodes = list(set([int(line.split('\t')[0]) for line in composed]))

    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    return G

def main():
    if __name__=="__main__":

        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-c', '--composed', help='path to a file with composed transducer', required=True)
        parser.add_argument('-o', '--output', help='path to the output file', default='stdout')

        args = parser.parse_args()
        
        path = args.composed

        G = read_graph(path)
        arbor = nx.minimum_spanning_arborescence(G, attr='weight')
        nx.write_graphml(arbor, 'minimal_arb.graphml') 

main()

