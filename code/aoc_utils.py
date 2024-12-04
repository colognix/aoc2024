
# basic formatting
def prepare_line(line, day):
    # remove linebreaks (windows..)
    line = line.replace('\n','')

    # remove whitespaces
    if day in []:
        line = line.replace(' ','')

    # remove redundant trailing info followed by ':'
    if day in []:
        line = line.split(':')[1]

    # matrix
    if day in [4]:
        line = [c for c in line]
        
    # whitespace seperated values
    elif day in [1,2]:
        line = line.split()
        
    # key-value like line [str,int]
    if day in []:
        line = [line[0],int(line[1])]

    # convert chars to numbers
    if day in [1,2]:
        line = [int(s) for s in line]

    return line

def read_input(path_base, day):
    path = path_base + str(day) + '.txt'
    with open(path,'r') as f:
        return [prepare_line(line,day) for line in f.readlines()]
