#imports
from collections import namedtuple

# 1	From	from	ADP	IN	_	3	case	3:case	_
# (index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2)
Conll = namedtuple('Conll', 'index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2')
labels = ['nsubj', 'obj', 'iobj', 'csubj', 'ccomp', 'xcomp', 'obl', 'vocative', 'expl', 'dislocated', 'advcl', 'advmod', 'discourse',
'aux', 'cop', 'mark', 'nmod', 'appos', 'nummod', 'acl', 'amod', 'det', 'clf', 'case', 'conj', 'cc', 'fixed', 'flat', 'compound',
'list', 'parataxis', 'orphan', 'goeswith', 'reparandum', 'punct', 'root', 'dep']

# open file given as function parameter
with open('../ud-treebanks-v2.4/UD_English-EWT/en_ewt-ud-test.conllu', 'r', encoding='utf8') as f:
    sentences = f.read().split('\n\n')

# extract Conll named tuple for each sentence in the read file
# sentences = [[Conll(*x.split('\t')) for x in s.split('\n') if x and not x.startswith('#')]
#              for s in sentences]

sentences = [[Conll(*x.split('\t')) for x in s.split('\n') if x and not x.startswith('#')]
             for s in sentences]

# 0	1	@^@	@^@	0.0
# 1	2	t	t	0.0
# 2	3	h	h	0.0
# 3	4	e	e	0.0
# 4	5	DET	DET	0.0
# 5	11	@det	@det	0.0
# 5	11	@nsubj	@nsubj	0.0
# 5	6	@$@	@$@	0.0
# 6	7	@^@	@^@	0.0
# 7	8	d	d	0.0
# 8	9	o	o	0.0
# 9	10	g	g	0.0
# 10	11	NOUN	NOUN	0.0
# 11	5	@det	@det	0.0
# 11	5	@nsubj	@nsubj	0.0
# 11	12	@$@	@$@	0.0
# 12	0.0

hfsts = []
for sentence in sentences:
    i = 0
    pos_loc = []
    hfst = []
    hfst_word = ""
    for conll in sentence:
        hfst_word += str(i) + '\t' + str(i+1) + "\t@^@\t@^@\t0.0\n"  # start of word
        i += 1

        # split the word into characters
        for c in conll.word:
            hfst_word += str(i) + '\t' + str(i+1) + '\t' + c + '\t' + c + '\t0.0\n'
            i += 1

        # add the POS tag
        hfst_word += str(i) + '\t' + str(i+1) + '\t' + conll.pos + '\t' + conll.pos + '\t0.0\n'
        i += 1

        # record the locations of the POS tags
        pos_loc.append(i)

        # if not pos_loc:
        #     pos_loc.append(len(conll.word) + 2)  # location of first POS tag
        # else:
        #     # dynamic programming! yaaaaay
        #     pos_loc.append(pos_loc[-1] + len(conll.word) + 3)

        hfst.append(hfst_word)

        hfst_word = str(i) + '\t' + str(i+1) + "\t@$@\t@$@\t0.0\n"
        i += 1

    assert len(hfst) == len(pos_loc)

    end = hfst_word + str(i) + '\t0.0'

    new_hfst = ""
    for i, word in enumerate(hfst):
        new_hfst += word
        x = pos_loc[i]
        for y in pos_loc:
            if x == y: continue
            for label in labels:
                new_hfst += str(x) + '\t' + str(y) + '\t' + label + '\t' + label + '\t1.0\n'

    new_hfst += end

    hfsts.append(new_hfst)

assert len(hfsts) == len(sentences)

for i, out_hfst in enumerate(hfsts):
    with open('../hfsts/' + str(i) + '.txt', 'w', encoding='utf8') as out_file:
        out_file.write(out_hfst)
