import itertools
DEBUG = False
if DEBUG:
    debug_print = print
else:
    def debug_print(*args): pass

def load_data():
    return [
        {1, 2, 3, 4},
        {1, 2, 4},
        {1, 2},
        {2, 3, 4},
        {2, 3},
        {3, 4},
        {2, 4}
    ]

DATA = load_data()
ITEMS = { ele for row in DATA for ele in row }

def support_count(item):
    return sum(1 for row in DATA if item.issubset( row ))

def confidence(rule):
    # rule: 2-tuple
    # where rule[0] = set of items
    #       rule[1] = set of items
    return support_count(rule[0] | rule[1]) / support_count(rule[1])

def apriori(data, min_sup=3, min_conf=0.70):

    print('Min. Support =', min_sup, 'Min. Confidence =', min_conf)

    freq_table = dict()
    for k in range(1, len(DATA)):
        debug_print('k=', k)
        # freq_table = dict()
        new_table = dict()
        for item in itertools.combinations(ITEMS, r=k):
            debug_print('item', item)
            ans = support_count(set(item)) # * len(DATA)
            if ans >= min_sup: 
                new_table[item] = ans
        if not new_table: # if empty dict
            break
        else:
            freq_table = new_table
        debug_print(freq_table)

    print('Final candidates:')
    for item in freq_table:
        print(item, 'Support Count:', freq_table[item])
    k_size = len(item) # Get largest k_size yet

    print('Association rules:')
    rules = []
    for itemset in freq_table:
        debug_print('Itemset:', itemset)
        for i in range(1, k_size):
            for item in itertools.combinations( itemset, r=i):
                lhs, rhs = set(item), set(itemset) - set(item)

                debug_print('\titem:', item)
                debug_print('\t\trule:', lhs, '->', rhs)

                rules.append( (lhs, rhs) )

    for rule in rules:
        print(rule[0], '->', rule[1], end=' ')
        print('Confidence:', '{:5.2f}'.format( confidence(rule) ))

    print('Chosen rules:')
    chosen_rules = [rule for rule in rules if confidence(rule) >= min_conf]
    for rule in chosen_rules:
        print(rule[0], '->', rule[1], end=' ')
        print('Confidence:', '{:5.2f}'.format( confidence(rule) ))

if __name__ == '__main__':
    apriori(data=DATA, min_sup=3, min_conf=0.70)
