import os.path
from copy import deepcopy

input_file = os.path.dirname(os.path.realpath(__file__)) + "/ExampleInput.txt"
input_file = os.path.dirname(os.path.realpath(__file__)) + "/MyInput.txt"

stack = []
stack.append(['D', 'L', 'V', 'T', 'M', 'H', 'F'])
stack.append(['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P'])
stack.append(['R', 'S', 'D', 'M', 'P', 'H'])
stack.append(['L', 'B', 'V', 'F'])
stack.append(['N', 'H', 'G', 'L', 'Q'])
stack.append(['W', 'B', 'D', 'G', 'R', 'M', 'P'])
stack.append(['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q'])
stack.append(['C', 'L', 'W'])
stack.append(['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T'])

stack_part2 = deepcopy(stack)

with open(input_file) as data_set:
    
    for line in data_set.readlines():
        parts = line.split(' ')
        
        if parts[0] == 'move':
            count = int(parts[1])
            from_index = int(parts[3]) - 1
            to_index = int(parts[5]) - 1 

            for _ in range(count):
                pop = stack[from_index].pop()
                stack[to_index].append(pop)

    result = ''
    for turm in stack: result = result + turm[-1]
    print("Result of part 1: ", result)

#Part 2
with open(input_file) as data_set:
    
    for line in data_set.readlines():
        parts = line.split(' ')
        
        if parts[0] == 'move':
            count = int(parts[1])
            from_index = int(parts[3]) - 1
            to_index = int(parts[5]) - 1 

            pop_temp= []
            for _ in range(count):
                pop = stack_part2[from_index].pop()
                pop_temp.append(pop)

            pop_temp.reverse()
            for i in pop_temp: stack_part2[to_index].append(i)           
    
    result = ''
    for turm in stack_part2: result = result + turm[-1]
    print("Result of part 2: ", result)