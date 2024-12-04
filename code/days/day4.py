from days.base import Basesolver
import re
import numpy as np

class Solver(Basesolver): 
    # process input, override if neccessary
    def process_input(self,input):
        self.input = np.array(input)

    # declare constant stuff for both parts
    def set_constants(self):
        # part 1
        self.re_xmas_forward = re.compile('XMAS')
        self.re_xmas_backward = re.compile('SAMX')

        # part 2
        self.sms = ['SM','MS']

    # set part for checks and also load part dependent stuff, override if neccessary
    def set_part(self,part):
        self.part = part

    # solvers for parts, need to be overwritten
    def solve_1(self):
        scan_lines = []
        
        # horizontal lines
        scan_lines += [''.join(l) for l in self.input]
        # vertical lines
        scan_lines += [''.join([l[i] for l in self.input]) for i in range(len(self.input))]

        # diagonals
        diags_r = [self.input.diagonal(i) for i in range(4-len(self.input),len(self.input)-3)]
        diags_l = [np.flipud(self.input).diagonal(i) for i in range(4-len(self.input),len(self.input)-3)]

        scan_lines += [''.join(d) for d in diags_r]
        scan_lines += [''.join(d) for d in diags_l]

        # create scan string
        scan = ' '.join(s for s in scan_lines)
        
        return len(self.re_xmas_forward.findall(scan)) + len(self.re_xmas_backward.findall(scan))
    
    def solve_2(self):
        xmas_count = 0
        n = len(self.input)
        for i,j in zip(*np.where(self.input == 'A')):
            if i > 0 and j > 0 and i < n-1 and j < n-1 and self.check_xmas(i,j):
                xmas_count += 1
        return xmas_count
    
    def check_xmas(self,i,j):
        X = [self.input[i-1,j-1]+self.input[i+1,j+1],self.input[i-1,j+1]+self.input[i+1,j-1]]
        return len([side for side in X if side in self.sms]) == 2
