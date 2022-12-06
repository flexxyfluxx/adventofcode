import readops as rops


def parse_stack_line(line: str) -> list[str]:
    layer = []
    
    for chunk in rops.chunks(line, 4):
        layer.append(chunk[1])
    
    return layer

def create_stacks(*layers: list[str]) -> list[list[str]]:
    stacks = [[] for _ in range(9)] # init empty stacks. we have 9 stacks => make 9 stacks
    for layer in layers:
        for idx, item in enumerate(layer):
            if item.strip():
                stacks[idx].append(item)
    
    return [list(reversed(stack)) for stack in stacks]

def parse_op_line(line: str):
    tokens = line.split(" ")
    
    # Since we have an invariable syntax, we can derive meaning from position alone.
    # map to dict for descriptiveness reasons.
    # sub 1 from src and dest because we store 
    return {'amount': int(tokens[1]), 'src': int(tokens[3])-1, 'dest': int(tokens[5])-1}
    
def exec_op(stacks, op):
    for _ in range(op['amount']):
        stacks[op['dest']].append(stacks[op['src']].pop())
    
def _main1():
    lines = list(rops.read_lines_from_file("data.txt", True))
    lines_divided = [[],[]]
    for idx, line in enumerate(lines):
        if not line:
            break
        
        lines_divided[0].append(line)
    
    lines_divided[1] = lines[idx+1:]
    
    stack_lines = lines_divided[0][:-1]
    op_lines = lines_divided[1]
    
    stacks = create_stacks(*[parse_stack_line(line) for line in stack_lines])
    ops = [parse_op_line(line) for line in op_lines]
    
    for op in ops:
        exec_op(stacks, op)
        
    for stack in stacks:
        print(stack[-1], end="")
    print("\n")
    
# --- PART 2 ---

def exec_op_multilift(stacks, op):
    movestack = []
    for _ in range(op['amount']):
        movestack.append(stacks[op['src']].pop())
        
    movestack.reverse()
    stacks[op['dest']] += movestack

def _main2():
    lines = list(rops.read_lines_from_file("data.txt", True))
    lines_divided = [[],[]]
    for idx, line in enumerate(lines):
        if not line:
            break
        
        lines_divided[0].append(line)
    
    lines_divided[1] = lines[idx+1:]
    
    stack_lines = lines_divided[0][:-1]
    op_lines = lines_divided[1]
    
    stacks = create_stacks(*[parse_stack_line(line) for line in stack_lines])
    ops = [parse_op_line(line) for line in op_lines]
    
    for op in ops:
        exec_op_multilift(stacks, op)
        
    for stack in stacks:
        print(stack[-1], end="")
    print("\n")

### EXEC SECTION ###
main = {
    1: _main1,
    2: _main2
}

part = 2
if __name__ == "__main__" and part:
    main[part]()