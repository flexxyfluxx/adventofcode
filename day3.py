import readops as fops
import string

# --- PART 1 ---

def split_str_in_half(string: str) -> tuple[str]:
    len_of_half_of_str: int = len(string) // 2
    return (string[:len_of_half_of_str], string[len_of_half_of_str:])

def get_duplicate_in_backpack(backpack: str) -> str:
    pockets = split_str_in_half(backpack)

    for item in pockets[0]:
        if item in pockets[1]:
            return item
        # since we know that there is exactly one duplicate per backpack,
        # we can immediately return when we find a dupe.

# thank you string.ascii_letters for existing~~~
PRIOMAP = {letter: (prio+1) for prio, letter in enumerate(string.ascii_letters)}

def _main1():
    lines = fops.read_lines_from_file("data.txt", True)

    line_duplicates = [get_duplicate_in_backpack(line) for line in lines]

    print(sum(PRIOMAP[duplicate] for duplicate in line_duplicates))


# --- PART 2 ---

# make it flexible for any amount of backpack per group because why the actual fuck not.
def get_duplicate_across_multiple_backpacks(*backpacks):
    for item in backpacks[0]:
        if all(item in backpack for backpack in backpacks[1:]):
            return item
                

def _main2():
    
    lines = fops.read_lines_from_file("data.txt", True)
                                        # this code is from stackoverflow lmao
    backpack_groups: list[list[str]] = [lines[i:i+3] for i in range(0, len(lines), 3)]

    badges = [get_duplicate_across_multiple_backpacks(*backpack_group) for backpack_group in backpack_groups]

    print(sum([PRIOMAP[badge] for badge in badges]))


### EXEC SECTION ###
main = {
    1: _main1,
    2: _main2
}

part = 2
if __name__ == "__main__":
    main[part]()