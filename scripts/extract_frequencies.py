from collections import Counter, namedtuple


def print_freqs(freqs):
    with open('frequencies.csv', 'w') as f:
        for t, c in freqs.items():
            print(str(t), file=f)
            for k, v in c.most_common():
                print('\t' + str(k) + ':\t' + str(v), file=f)

#  (dep_POS, arc_label, head_POS)
Arc = namedtuple('Arc', 'dep_POS, head_POS')

# 1	From	from	ADP	IN	_	3	case	3:case	_
# (index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2)
Conll = namedtuple('Conll', 'index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2')


def extract_freqs(file):
    '''
    Returns a counter of dependency arc frequencies found in file
    :return: Counter of Dep Arcs
    '''
    with open(file ,'r', encoding='utf8') as f:
        sentences = f.read().split('\n\n')

    sentences = [[Conll(*x.split('\t')) for x in s.split('\n') if x and not x.startswith('#')]
                 for s in sentences]
    # print(sentences[2])

    freqs = Counter()

    arcs = {}
    for sentence in sentences:
        for c in sentence:
            # skip parataxis words
            if '.' in c.index:
                continue
            try:
                arc = Arc(c.pos, sentence[int(c.head_index)-1].pos)
                if not arc in arcs:
                    arcs[arc] = []
                arcs[arc].append(c.arc_label)
            except ValueError as e:
                print(sentence)
                print(e)
                print(c)

    freqs = {k: Counter(v) for k, v in arcs.items()}
    return freqs

if __name__== "__main__":
    freqs = extract_freqs('../ud-treebanks-v2.4/UD_English-EWT/en_ewt-ud-train.conllu')
    print_freqs(freqs)