'''
input:
    A B C
    0 1 1
    0 0 1
    1 0 0
'''
DEBUG = False
debug_print = print if DEBUG else lambda *x: None
class Node:
    def __init__(self, name):
        # inb = list of strings of node names
        self.name = name
        self.inb = [] # inbound
        self.oub = [] # outbound

    def __repr__(self):
        return f'Node(name={self.name}, inbound={self.inb}, outbound={self.oub}'

def page_rank(nodes, iterlimit, d=0.85):
    fstr= '{:9d} ' + '{:1.6f} ' * len(nodes)
    pr = [1 for _ in nodes]
    fhead = '{:9s} ' + '{:8s} ' * len(nodes)
    
    headlist = ['Node ' + str(ni) for ni in range(len(nodes))]
    print( fhead.format('Iteration', *headlist ) )
    for iter_no in range(iterlimit):
        
        for ni, node in enumerate(nodes):
            ans = sum( pr[pi] / len(nodes[pi].oub) for pi in node.inb )
            pr[ni] = (1-d) + d * ans
        print(fstr.format(iter_no, *pr))
            

if __name__ == '__main__':
    mat = [[0,1,1],
           [0,0,1],
           [1,0,0]]
    nodes = [Node(str(i)) for i,_ in enumerate(mat)]
           
    for ri, row in enumerate(mat):
        for ci, col in enumerate(row):
            if col == 1:
                nodes[ri].oub.append(ci)
                nodes[ci].inb.append(ri)
    
    for n in nodes:
        debug_print(n)
        
    page_rank(nodes, iterlimit=3, d=0.85)
        
'''
Output:
Iteration Node 0   Node 1   Node 2
        0 1.000000 0.575000 1.063750
        1 1.054187 0.598030 1.106355
        2 1.090402 0.613421 1.134828
'''        