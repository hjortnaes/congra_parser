
import sys 

def form(s):
	t = {'@^@':'^','@$@':'$','@_IDENTITY_SYMBOL_@':'?'}
	o = s
	for i in t:
		o = o.replace(i, t[i])
	return o

nodes = []
print('''
digraph G {
    rankdir=LR;
    graph[fontname="Tahoma"];
''')
for line in sys.stdin.readlines():
	
	row = line.strip('\n').split('\t')
	if len(row) == 5:
		print('%s -> %s [ label="%s:%s/%s" ];' % (row[0], row[1], form(row[2]), form(row[3]), row[4]))
		nodes.append(row[0])
	elif len(row) == 2:
		print('%s [shape =doublecircle, style=filled, color=black, fillcolor=gray];' % (row[0]));

for node in nodes:
	print('%s [shape=circle, style=filled, color=black, fillcolor=gray];' % (node))

print('}')
