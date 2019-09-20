all:
	hfst-txt2fst minimal_rule.txt -o minimal_rule.hfst
	hfst-txt2fst example.txt -o example.hfst
	hfst-compose -1 example.hfst -2 minimal_rule.hfst | hfst-fst2txt
