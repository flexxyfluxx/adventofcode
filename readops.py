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

def single_string_read_file(filename: str, strip_file: bool):
    with open(filename) as f:
        file_contents = f.read()
    
    if strip_file:
        return file_contents.strip()
    return file_contents
    

def chunks(arr: list[any], chunksize: int) -> list[list[any]]:
    for c in range(0, len(arr), chunksize):
        yield arr[c:c+chunksize]

def wide_read(iterable: list[any] | str, headwidth: int):
    start = 0
    for start in range(len(iterable) - headwidth):
        yield iterable[start:start+headwidth]
        start += 1