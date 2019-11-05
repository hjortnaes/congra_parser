#imports

# 1	From	from	ADP	IN	_	3	case	3:case	_
# (index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2)
Conll = namedtuple('Conll', 'index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2')

# open file given as function parameter
with open('../ud-treebanks-v2.4/UD_English-EWT/en_ewt-ud-train.conllu', 'r', encoding='utf8') as f:
    sentences = f.read().split('\n\n')

# extract Conll named tuple for each sentence in the read file
sentences = [[Conll(*x.split('\t')) for x in s.split('\n') if x and not x.startswith('#')]
             for s in sentences]

for sentence in sentences:

    pass
