from collections import namedtuple
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def recreate_sent(path, mst):
    dependency = re.compile(r'@\w+')
    pos = re.compile(r'[A-Z]+')
    Word = namedtuple('Word', ['index', 'word', 'lem',\
                               'pos', 'head', 'rel', 'deprel'])
    
    
    word = Word('', '', '', '', '', '' ,'')
    curr_w = ''
    curr_pos = ''
    
    conll = []
    
    with open(path, 'r') as fo:
        for line in fo.readlines()[:-1]:
            line = line.split('\t')
            if line[2][0] != '@' and not re.findall(pos, '\t'.join(line)):
                curr_w+=line[2][0]
            elif line[2][0] != '@' and re.findall(pos, '\t'.join(line)):
                curr_pos+=line[2]
                
            elif re.findall(dependency, line[2]):
                word = word._replace(word = curr_w)
                word = word._replace(lem = lemmatizer.lemmatize(curr_w))
                curr_w=''
                word = word._replace(pos = curr_pos)
                curr_pos=''
                
                node = {'par':line[0], 'label':line[2]}
                if line[1] in mst and word.word:
                    word = word._replace(index = line[1])
                    word = word._replace(head = mst[line[1]]['par'])
                    word = word._replace(rel = mst[line[1]]['label'][1:])
                    word = word._replace(deprel = word.head+':'+mst[line[1]]['label'][1:])
                    
                    conll_str = '\t'.join([word.index,
                                            word.word,
                                            word.lem,
                                            word.pos,
                                            '_', '_',
                                            word.head,
                                            word.rel, 
                                            word.deprel])
                    conll.append(conll_str)
                else:
                    continue
    return conll

def update_index(parse):
    parse = [c.split('\t') for c in parse]
    mapping = {s[0]:str(i+1) for i, s in enumerate(parse)}
    change_ind = []
    for c in parse:
        init_ind = mapping[c[0]]
        try:
            rel_ind = mapping[c[6]]
            c.pop(0)
            c.insert(0, init_ind)
            c.pop(6)
            c.insert(6, rel_ind)
            tag = c[-1].split(':')[-1]
            c.pop(-1)
            c.append(rel_ind+':'+tag)
            change_ind.append(c)

        except KeyError:
            c.pop(0)
            c.insert(0, init_ind)
            change_ind.append(c)
            continue
    return '\n'.join(['\t'.join(sent) for sent in change_ind])