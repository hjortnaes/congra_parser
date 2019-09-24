
import sys, graphviz

def form(s):
	t = {'@^@':'^','@$@':'$','@_IDENTITY_SYMBOL_@':'?','@0@':'ε'}
	o = s
	for i in t:
		o = o.replace(i, t[i])
	return o

nodes = []
dot = graphviz.Digraph(graph_attr={'rankdir':'LR'},node_attr={'fontname':'Tahoma'},edge_attr={'fontname':'Courier New'});

for line in open(sys.argv[1]).readlines():
	row = line.strip('\n').split('\t')
	if len(row) == 5:
		if row[2] == row[3]:
			dot.edge(row[0], row[1], label="%s/%s" % (form(row[2]), row[4]))
		else:
			dot.edge(row[0], row[1], label="%s:%s/%s" % (form(row[2]), form(row[3]), row[4]))
		nodes.append(row[0])
	elif len(row) == 2:
		dot.node(row[0], shape="doublecircle", style="filled", color="black", fillcolor="gray")

for node in nodes:
	dot.node(node, shape="circle", style="filled", color="black", fillcolor="grey")


dot.view()
