from days.base import Basesolver
import re

class Solver(Basesolver): 
    # process input, override if neccessary
    def process_input(self,input):
        self.input = ''.join(input)

    # declare constant stuff for both parts
    def set_constants(self):
        self.mul_regex = re.compile('mul\(\d+,\d+\)')

    # solvers for parts, need to be overwritten
    def solve_1(self):        
        return self.get_mul(self.input)
    
    def solve_2(self):
        s = 0
        # split by don'ts
        donts = self.input.split('don\'t()')
        # before first don't everythings executed
        s += self.get_mul(donts[0])
        # for every don't
        for dont in donts[1:]:
            dos = dont.split('do()')
            # only do stuff after a do
            for do in dos[1:]:
                s += self.get_mul(do)

        return s
    
    # for a given string: find all "mul(\d,\d)", convert to numbers, multiply and add up
    def get_mul(self,s):
        muls = self.mul_regex.findall(s)
        vals = [m.replace('mul(','').replace(')','').split(',') for m in muls]
        return sum([int(v[0])*int(v[1]) for v in vals])