from typing import List, Tuple

def list_to_file(str_list: List[str], filename:str):
    with open(filename, "w") as f:
        for s in str_list:
            f.write(s + "\n")

def list_from_file(filename:str):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines

