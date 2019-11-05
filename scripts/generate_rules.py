from scripts.extract_frequencies import extract_freqs


freqs = extract_freqs('../ud-treebanks-v2.4/UD_English-EWT/en_ewt-ud-train.conllu')

# Have to get each Arc head and head arc pair -
for k, labels in freqs.items():
    rule = """0	1	@^@	@^@	0.0
1	1	@_IDENTITY_SYMBOL_@	@_IDENTITY_SYMBOL_@	0.0
1	2	{dep}	{dep}	0.0""".format(dep=k.dep_POS)
    for arc_label, freq in labels.items():
        rule += "\n2	7	@{label}	@{label}	{val}".format(label=arc_label, val=freq)
    rule += """
2	3	@$@	@$@	0.0
2	5	@$@	@$@	0.0
3	4	@^@	@^@	0.0
4	4	@_IDENTITY_SYMBOL_@	@_IDENTITY_SYMBOL_@	0.0
4	5	@$@	@$@	0.0
5	3	@0@	@0@	0.0
5	6	@^@	@^@	0.0
6	6	@_IDENTITY_SYMBOL_@	@_IDENTITY_SYMBOL_@	0.0
6	7	{head}	{head}	0.0""".format(head=k.head_POS)
    for arc_label, freq in labels.items():
        rule += "\n7	2	@{label}	@{label}	{val}".format(label=arc_label, val=freq)
    rule += """
7	8	@$@	@$@	0.0
8	0.0"""
    with open('../rules/' + k.dep_POS + '_' + k.head_POS + '.txt', 'w', encoding='utf8') as rule_file:
        print(rule, file=rule_file)