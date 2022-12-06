import readops as rops

def all_in_sequence_unique(seq):
    for elem in seq:
        if seq.count(elem) > 1:
            return False
    return True

def _main1():
    msg = rops.single_string_read_file("data.txt", False)
    
    for idx, seq in enumerate(rops.wide_read(msg, 4)):
        if all_in_sequence_unique(seq):
            print(idx+4)
            break

# --- PART 2 ---


def _main2():
    msg = rops.single_string_read_file("data.txt", False)
    
    for idx, seq in enumerate(rops.wide_read(msg, 14)):
        if all_in_sequence_unique(seq):
            print(idx+14)
            break

### EXEC SECTION ###
main = {
    1: _main1,
    2: _main2
}

part = 2
if __name__ == "__main__" and part:
    main[part]()