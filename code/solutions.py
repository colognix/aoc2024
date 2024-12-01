import aoc_utils
from importlib import import_module

def solve (day, example=False):
    if (example):
        input = aoc_utils.read_input('./input/examples/day', day)
    else:
        input = aoc_utils.read_input('./input/day', day)

    day = import_module('days.day'+str(day))
    solver = day.Solver(input)
    print(solver.solve())
    solver.set_part(2)
    print(solver.solve())

solve(1,False)