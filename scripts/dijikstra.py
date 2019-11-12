nodes = ['A', 'B', 'R']
edges = [(1, 'R', 'A'), (1, 'R', 'B'), (40, 'A', 'B'), (50, 'A', 'B'),
              (10, 'B', 'A'), (20, 'B', 'A')]



#Min heap structure

class heap:
    def __init__(self):
        self.store = []
        
    def push(self, val):
        self.store.append(val)
        i = len(self.store)-1
        
        while(i>=0):
            if self.store[i]['weight'] < self.store[(i-1)//2]['weight']:
                temp = self.store[i]
                self.store[i] = self.store[(i-1)//2]
                self.store[(i-1)//2] = temp
            i = (i-1)//2
    
    def pop(self):
        return self.store.pop(0)
    
    def isEmpty(self):
        return len(self.store) == 0




def djikstra(G, sn):
    G_h = {}
    for i in G:
        if i == sn:
             G_h[i] = {'par':"", "wt":0}
        else:
            G_h[i] = {'par':"", "wt":999999999}
    nodes = [sn]+[i for i in G if i != sn]
    for par in nodes:
        children = G[par]
        H = heap()
        for child in children:
            H.push(child)
        while(not H.isEmpty()):
            curr = H.pop()
            if G_h[curr['dest']]['wt'] >= G_h[curr['par']]['wt'] + curr['path_cost']:
                G_h[curr['dest']]['par'] = curr['par']
                G_h[curr['dest']]['wt'] = G_h[curr['par']]['wt'] + curr['path_cost']
    
    return G_h   

##Subtract weights from the max value

def max_weight(edges):
    max_edge = max([e[0] for e in edges])
    print(max_edge)
    d =  [(max_edge - e[0], e[1], e[2]) for e in edges]
    print(d)
    return d 

edges = max_weight(edges)

G = {n:[] for n in nodes}
#Convert to graph
for e in edges:
    G[e[1]].append({'dest':e[2], 'path_cost':e[0], 'weight':999999999, 'par':e[1]})

