import csv

def load_csv(c_file):
    data = {}
        # 'CarNo': [], 'Color': [], 
        # 'Type': [], 'Origin': [], 'Stolen': []}
    with open(c_file) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key, value in row.items():
                data.setdefault(key, []).append(value)
            # data['CarNo'].append(row[0])
            # data['Color'].append(row[1])
            # data['Type'].append(row[2])
            # data['Origin'].append(row[3])
            # data['Stolen'].append(row[4])
    del data['Car No']
    return data

def predict(data, Color, Type, Origin):
    ans = {'Yes': -1, 'No': -1}


    for output in ans:
        lstolen = data['Stolen']
        lcolor = data['Color']
        ltype = data['Type']
        lorigin = data['Origin']

        poutput = lstolen.count(output) / len(lstolen)
        pcolor  = get_intersect_probability(lcolor, lstolen, Color, output)   / poutput
        ptype   = get_intersect_probability(ltype, lstolen, Type, output)     / poutput
        porigin = get_intersect_probability(lorigin, lstolen, Origin, output) / poutput
        pfinal = pcolor * ptype * porigin * poutput
        ans[output] = pfinal

        fstr1 = (f'P({Color}/{output}) * P({Type}/{output}) * '
                f'P({Origin}/{output}) * P({output})')
        fstr2 = (f'= {pcolor} * {ptype} * {porigin} * {poutput}')
        fstr3 = f'= {pfinal}'
        print(fstr1, fstr2, fstr3, sep='\n')
        
    return max(ans, key=lambda x: ans[x])

def get_intersect_probability(a1, a2, v1, v2):
    '''
    Find intersection probabilities of two lists/events
    a1,a2 are two lists
    v1,v2 are values to be equal at same position in both lists
    '''
    # c = 0
    # for x,y in zip(a1, a2):
    #     if x == v1 and y == v2:
    #         c += 1
    # return c / len(a1)
    return sum(1 for x,y in zip(a1,a2) if x == v1 and y == v2 ) / len(a1)

if __name__ == '__main__':
    c_file = 'cars.csv'
    data = load_csv(c_file)
    print('Predict:', 'Red', 'SUV', 'Domestic')
    pred = predict(data=data, Color='Red', Type='SUV', Origin='Domestic')
    print('Stolen?:', pred)

'''
Predict: Red SUV Domestic
P(Red/Yes) * P(SUV/Yes) * P(Domestic/Yes) * P(Yes)
= 0.6 * 0.2 * 0.4 * 0.5
= 0.024
P(Red/No) * P(SUV/No) * P(Domestic/No) * P(No)
= 0.4 * 0.6 * 0.6 * 0.5
= 0.072
Stolen?: No
'''