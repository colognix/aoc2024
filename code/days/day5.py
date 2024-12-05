from days.base import Basesolver

class Solver(Basesolver): 
    # process input, override if neccessary
    def process_input(self,input):

        self.orders = {}
        self.updates = []
        self.unclean_updates = []
        self.cleaned_updates = []

        for l in input:
            if '|' in l:
                tmp = l.split('|')
                self.add_order(int(tmp[1]),int(tmp[0]))
            if ',' in l:
                self.updates += [[int(p) for p in l.split(',')]]  

    # solvers for parts, need to be overwritten
    def solve_1(self):
        print_sum = 0
        for u in self.updates:
            i = self.find_missalignment(u)
            if  i < 0:
                print_sum += u[int(len(u)/2)]
            else:
                self.unclean_updates += [[u,i]]

        return print_sum
    
    def solve_2(self):
        print_sum = 0
        for uu in self.unclean_updates:
            i = uu[1]
            u = uu[0]
            while i >= 0:
                u = self.clean_update(u,i)
                i = self.find_missalignment(u)
            print_sum += u[int(len(u)/2)]
        return print_sum
    
    def add_order(self,x,y):
        try:
            self.orders[x] += [y]
        except KeyError:
            self.orders[x] = [y]

    def find_missalignment(self,u):
        # find correct spot
        for i in range(len(u)):
            try:
                if set(self.orders[u[i]]) & set(u[i+1:]):
                    return i
            except KeyError:
                continue
        return -1

    def clean_update(self,u,i):
        # remove false page
        v = u.pop(i)
        # find correct spot
        for j in range(i,len(u)):
            try:
                if not (set(self.orders[v]) & set(u[j+1:])):
                    u.insert(j+1,v)
                    break
            except KeyError:
                u.insert(j+1,v)
                break
        return u
