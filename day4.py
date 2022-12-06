import readops as fops

def parse_line(line):
    # init data structures

    partners_raw = [[int(num) for num in partner.split("-")] for partner in (line.split(","))]

    # return array of partners as dicts. more descriptive this way.
    return [
        {
            'start': partners_raw[c][0],
            'end': partners_raw[c][1]
        }
        for c in range(2)
    ]

def does_contains_other(min0, max0, min1, max1):
    return min0 <= min1 and max0 >= max1 \
        or min0 >= min1 and max0 <= max1


def _main1():
    file = fops.read_lines_from_file("data.txt", True)

    pairs = [parse_line(line) for line in file]
    contains_boolmap = [
        does_contains_other(
            pair[0]['start'],
            pair[0]['end'],
            pair[1]['start'],
            pair[1]['end']
        )
        for pair in pairs
    ]
    print(sum(contains_boolmap))

# --- PART 2 ---

def overlaps(min0, max0, min1, max1):
    # For an overlap to occur, the minimum of one must be in the range of the other.
    # We could've used maximums instead, too. It doesn't matter.
    return min1 <= min0 <= max1 \
        or min0 <= min1 <= max0

def _main2():
    file = fops.read_lines_from_file("data.txt", True)

    pairs = [parse_line(line) for line in file]
    overlaps_boolmap = [
        overlaps(
            pair[0]['start'],
            pair[0]['end'],
            pair[1]['start'],
            pair[1]['end']
        )
        for pair in pairs
    ]
    print(sum(overlaps_boolmap))


### EXEC SECTION ###
main = {
    1: _main1,
    2: _main2
}

part = 2
if __name__ == "__main__":
    main[part]()