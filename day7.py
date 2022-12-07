from dataclasses import dataclass
import readops as rops


@dataclass
class File:
    size: int

@dataclass
class Cmd:
    cmdstr: str
    result: list[str]

class Dir: ... # necessary to allow recursive datastructure definition in Dir

@dataclass
class Dir:
    children: dict[File|Dir]
    parent: Dir|None
    
    def add_child(self, name, child: File|Dir) -> None:
        self.children[name] = child

    def has_child_with_name(self, name: str) -> bool:
        return name in self.children.keys()

    def get_child_by_name(self, name: str) -> File|Dir:
        return self.children[name] 

class System:
    def __init__(self) -> None:
        self.root = Dir({}, None)
        self._read_head = self.root
        
    
    def eval_cmd(self, cmd: Cmd) -> None:
        cmd_tokens = cmd.cmdstr.strip().split(" ")[1:] # remove whitespace and $; tokenize

        
        match cmd_tokens[0]:
            case "ls":
                for line in (line_.split() for line_ in cmd.result):
                    if self._read_head.has_child_with_name(line[1]): continue
                    if line[0] == "dir":
                        self._read_head.add_child(line[1], Dir({}, self._read_head))
                        continue

                    self._read_head.add_child(line[1], File(line[0]))
                    
            case "cd":
                match cmd_tokens[1]:
                    case "..":
                        self._read_head = self._read_head.parent
                        return
                
                    case "/":
                        self._read_head = self.root
                            
                
                if not self._read_head.has_child_with_name(cmd_tokens[1]):
                    self._read_head.add_child(cmd_tokens[1], Dir({}, self._read_head))
                self._read_head = self._read_head.get_child_by_name(cmd_tokens[1])

        

def _main1():
    system = System()
    
    cmds = []
    start = True
    for line in rops.read_lines_from_file("data", True):
        if line[0] == "$":
            if not start:
                cmds.append(Cmd(current_cmd, current_results))
            start = False
            
            current_cmd = line
            current_results = []
            continue
        current_results.append(line)
    cmds.append(Cmd(current_cmd, current_results))
    
    for cmd in cmds:
        system.eval_cmd(cmd)
                
    
    

# --- PART 2 ---
def _main2():
    ...


### EXEC SECTION ###
main = {
    1: _main1,
    2: _main2
}

part = 2
if __name__ == "__main__" and part:
    main[part]()