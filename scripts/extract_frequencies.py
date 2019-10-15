from collections import Counter, namedtuple


def extract_arc():
    pass

#  (dep_POS, arc_label, head_POS)
Arc = namedtuple('Arc', 'dep_POS, arc_label, head_POS')

# 1	From	from	ADP	IN	_	3	case	3:case	_
# (index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2)
Conll = namedtuple('Conll', 'index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2')

with open('../ud-treebanks-v2.4/UD_English-EWT/en_ewt-ud-dev.conllu',
          'r', encoding='utf8') as f:
    sentences = f.read().split('\n\n')

sentences = [[Conll(*x.split('\t')) for x in s.split('\n') if x and not x.startswith('#')]
             for s in sentences]
print(sentences[2])

freqs = Counter()

for sentence in sentences:
    arcs = []
    for c in sentence:
        arcs.append(Arc(c.pos, c.arc_label, sentence[int(c.head_index)-1].pos))
    freqs += Counter(arcs)

print(freqs)