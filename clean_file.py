#!/usr/bin/python
"""_summary_
"""


tfi = "A TreatyRight to Education.md"


def clean_file(tfi):
    """_summary_

    Args:
        tfi (str): file
    """
    return tfi.rstrip()


# first get all lines from file
with open('A TreatyRight to Education.md', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '  ') for line in lines]

# finally, write lines in the file
with open('A TreatyRight to Education.md', 'w') as f:
    f.writelines(lines)
