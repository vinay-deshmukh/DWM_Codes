import copy
def print_mean_dict(means):
    for k,v in means.items():
        print(k, '=', ' '.join(map(str,v)))

def mean(iterable): return sum(iterable) / len(iterable)

def kmeans(data, k):
    print('Original data:', data)
    partitions = [ data[i::k]  for i in range(k)]
    means = { mean(p) : p for p in partitions}

    iteration = 0
    while True:
        iteration += 1
        # Renew prev_means
        prev_means = copy.deepcopy(means)

        print('\nIteration:', str(iteration))
        print_mean_dict(means)

        means = {k : [] for k in means} # Clear the current clusters

        for ele in data:
            # Reassign data to closest means
            closest_mean = min(means, key=lambda k: abs(ele - k) )
            means[closest_mean].append(ele)

         # Recalculate means
        means = {mean(v):v for _, v in means.items() }

        if means == prev_means:
            break

    return means

data = [2,4,10,12,11,3,30,25,20]
a = kmeans(data, k=2)
print('\nAns:')
print_mean_dict(a)
'''
Original data: [2, 4, 10, 12, 11, 3, 30, 25, 20]

Iteration: 1
14.6 = 2 10 11 30 20
11.0 = 4 12 3 25

Iteration: 2
25.0 = 30 25 20
7.0 = 2 4 10 12 11 3

Ans:
25.0 = 30 25 20
7.0 = 2 4 10 12 11 3
'''