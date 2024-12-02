from days.base import Basesolver
import re
import numpy as np

class Solver(Basesolver): 
    # process input, override if neccessary
    def process_input(self,input):
        self.input = input

    # declare constant stuff for both parts
    def set_constants(self):
        return

    # set part for checks and also load part dependent stuff, override if neccessary
    def set_part(self,part):
        self.part = part

    # solvers for parts, need to be overwritten
    def solve_1(self):
        return self.input
    
    def solve_2(self):
        return self.input