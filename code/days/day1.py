from days.base import Basesolver
import numpy as np

class Solver(Basesolver):

    # process input, override if neccessary
    def process_input(self,input):
        self.input = np.array(input).T

    def solve_1(self):
        return sum(np.abs(np.subtract(np.sort(self.input[0]), np.sort(self.input[1]))))
    
    def solve_2(self):
        # left list
        numbers_left, counts_left = np.unique(self.input[0], return_counts=True)
        count_dict_left = dict(zip(numbers_left, counts_left))
        # right list
        # exclude numbers not in left list
        right_list = [n for n in self.input[1] if n in self.input[0]]
        numbers_right, counts_right = np.unique(right_list, return_counts=True)
        count_dict_right = dict(zip(numbers_right, counts_right))

        # compute similarity score 
        return (sum([count_dict_left[n]*count_dict_right[n]*n for n in count_dict_right.keys()]))
