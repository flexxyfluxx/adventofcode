def read_lines_from_file(filename: str, remove_whitespace: bool) -> list[int]:
    """
    This function takes a file name and returns a list of 
    """
    with open(filename) as f: # get all the lines
        all_lines: list[str] = f.readlines()

    if remove_whitespace:
        return [line.strip() for line in all_lines]

    return all_lines