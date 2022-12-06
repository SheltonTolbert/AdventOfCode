import sys

def parse_stacks(stacks):

    num_stacks = int(stacks[-2])
    parsed_stacks = []

    for i in range(num_stacks):
        # there is a more "pythonic" way to do this 
        # _parsed_stacks = [[]] * num_stacks_
        # but for some "pythonic" reason, that breaks things real bad
        parsed_stacks.append([])
    
    for stack in stacks.split('\n')[:-1]:
        for i in range(num_stacks):
            contents = stack[1 + (i * 4)]
            if (contents != ' '):
                parsed_stacks[i].insert(0, contents)

    return(parsed_stacks)

def execute_instructions(stacks, instructions):
    
    for instruction in instructions.split('\n')[:-1]:
        [_, quantity, _, source, _, destination] = instruction.split( ' ')
        crane = []

        for i in range(int(quantity)):
            crane.append(stacks[int(source) - 1].pop())

        for i in range(int(quantity)):
            stacks[int(destination) - 1].append(crane.pop())

    return stacks
     
def solve(input):
    [stacks, instructions] = input.split('\n\n')
    stacks = execute_instructions(parse_stacks(stacks), instructions)

    solution = ''
    for stack in stacks:
        solution += stack[-1]

    return solution

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    file = open(input_file_path)
    input = file.read()
    file.close()
    solution = solve(input)
    print(solution)
