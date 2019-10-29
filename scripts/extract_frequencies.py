from collections import Counter, namedtuple


def print_freqs(freqs):
    """
    Prints an easy to read format of the frequencies extracted from the corpus
    to the file frequencies.txt
    :return: None
    """
    with open('frequencies.txt', 'w') as f:
        for t, c in freqs.items():
            print(str(t), file=f)
            for k, v in c.most_common():
                print('\t' + str(k) + ':\t' + str(v), file=f)



### Declare useful named tuples
#  (dep_POS, arc_label, head_POS)
Arc = namedtuple('Arc', 'dep_POS, head_POS')

# 1	From	from	ADP	IN	_	3	case	3:case	_
# (index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2)
Conll = namedtuple('Conll', 'index, word, lemma, pos, og_pos, ignore, head_index, arc_label, enhanced_label, ignore_2')


def extract_freqs(file):
    '''
    Returns a dictionary of counters of dependency arc frequencies found in file
    First level of dict is arc head pairs, inner dict is frequencies of each label
    :return: Dict of Counters
    '''
    # open file given as function parameter
    with open(file ,'r', encoding='utf8') as f:
        sentences = f.read().split('\n\n')

    # extract Conll named tuple for each sentence in the read file
    sentences = [[Conll(*x.split('\t')) for x in s.split('\n') if x and not x.startswith('#')]
                 for s in sentences]
    # print(sentences[2])

    # extract all the arcs from the sentences and add them to lists
    arcs = {} # Key will be Arc Head pairs and value will be list of labels found
    for sentence in sentences:
        for c in sentence:
            # skip parataxis words
            if '.' in c.index:
                continue
            try:
                # get the arc head pair and add the label to the arc head pair list
                arc = Arc(c.pos, sentence[int(c.head_index)-1].pos)
                # if the arc head pair is not in the dict yet
                if not arc in arcs:
                    arcs[arc] = []
                arcs[arc].append(c.arc_label)
            except ValueError as e:
                print(sentence)
                print(e)
                print(c)

    # Pass each value in arcs to a Counter to generate label frequencies for each arc
    # head pair
    freqs = {k: Counter(v) for k, v in arcs.items()}
    return freqs

if __name__== "__main__":
    freqs = extract_freqs('../ud-treebanks-v2.4/UD_English-EWT/en_ewt-ud-train.conllu')
    print_freqs(freqs)