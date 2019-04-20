import copy
def print_mean_dict(means):
    for k,v in means.items():
        print(k, '=', ' '.join(map(str,v)))

def mean(iterable): 
    # for 1 d
    #return sum(iterable) / len(iterable)
    # for 2 d
    # iterable of (x,y)
    n = len(iterable)
    x, y = sum(p[0] for p in iterable), sum(p[1] for p in iterable)
    return x/n, y/n

def euclid(p1, p2): 
    return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

def kmeans(data, k, dimension):
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
            # if dimension == 1:
            #     closest_mean = min(means, key=lambda k: abs(ele - k) )
            if dimension == 2:
                closest_mean = min(means, key=lambda xy: euclid(xy, ele) )
            means[closest_mean].append(ele)

         # Recalculate means
        means = {mean(v):v for _, v in means.items() }

        if means == prev_means:
            break

    return means

# data = [2,4,10,12,11,3,30,25,20]
# a = kmeans(data, k=2, dimension=1)
# print('\nAns:')
# print_mean_dict(a)

data = [(1,1), (2,1), (4,3), (5,4)]
a = kmeans(data, k=2, dimension=2)
print('\nAns:')
print_mean_dict(a)

'''
1D DATA
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

'''
2D DATA
Original data: [(1, 1), (2, 1), (4, 3), (5, 4)]

Iteration: 1
(2.5, 2.0) = (1, 1) (4, 3)
(3.5, 2.5) = (2, 1) (5, 4)

Iteration: 2
(1.5, 1.0) = (1, 1) (2, 1)
(4.5, 3.5) = (4, 3) (5, 4)

Ans:
(1.5, 1.0) = (1, 1) (2, 1)
(4.5, 3.5) = (4, 3) (5, 4)
'''
