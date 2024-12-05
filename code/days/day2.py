from days.base import Basesolver

class Solver(Basesolver):

    def solve_1(self):
        safe_count = 0
        for report in self.input:
            if self.check_safety(report):
                safe_count += 1

        return safe_count
    
    def solve_2(self):
        safe_count = 0
        for report in self.input:
            if self.check_safety(report, True):
                safe_count += 1

        return safe_count
    
    
    def check_safety(self, report, dampener=False, old_diff = 0):
        for n in range(0,len(report)-1):
            diff = report[n+1] - report[n]
            if diff == 0 or abs(diff) > 3 or diff * old_diff < 0:
                if dampener:
                    # remove level at index n-1
                    if self.check_safety(report[:n-1] + report[n:]):
                        return True
                    # remove level at index n 
                    elif self.check_safety(report[:n] + report[n+1:]):
                        return True
                    # remove level at index n+1
                    elif self.check_safety(report[:n+1] + report[n+2:]):
                        return True
                    else:
                        return False
                else:
                    return False
            old_diff = diff
                    
        return True