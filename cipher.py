"""
    Author:     Caleb Otto-Hayes
    Date:       4/2/2021
"""

import re

def convert_text(string: str) -> str:
    """
        Converts text to upper-case, removing whitespace and 
        replacing a special character (eg. '.') into an 'X'.
        
        Returns the converted string.
    """

    # Regular expression pattern to remove numbers and spaces
    return re.sub(r'[^A-Za-z]+|[0-9]+|\s+', '', string.replace('.', 'X').upper())


def shift_text(string: str, key: int) -> str:
    shifted_str: str = ''
    
    for t in string:
        shifted_str += str((ord(t) + key) % 26)
    return shifted_str