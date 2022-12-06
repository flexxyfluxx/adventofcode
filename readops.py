def read_lines_from_file(filename: str, strip_line: bool) -> list[int]:
    """
    This function takes a file name and returns a list of 
    """
    with open(filename) as f: # get all the lines
        all_lines: list[str] = f.readlines()

    for line in all_lines:
        if strip_line:
            yield line.strip()
            continue

        yield line

def chunks(arr: list[any], chunksize: int) -> list[list[any]]:
    for c in range(0, len(arr), chunksize):
        yield arr[c:c+chunksize]