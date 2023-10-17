import re
import sys

'''
this file takes an input of a text file and searches for all of the iterations
of 'herit' with any prefixes and/or suffixes added to the word
it will return the words in a file with each iteration and the line number it
was found on
sys.argv[0] = python function
sys.argv[1] = text file
sys.argv[2] = file to print the list of words to
'''

def search_criteria(word):
    '''
    creates the search criteria and searches the file to find that word with
    any prefixes or suffixes
    '''
    pattern = r'\b\w*' + word + r'\w*\b'
    return pattern

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as origin_in:
        with open(sys.argv[2], 'w') as origin_out:
            pattern = search_criteria('herit')
            for line_number, line in enumerate(origin_in, start=1):
                matches = re.finditer(pattern, line, flags=re.IGNORECASE)
                for match in matches:
                    print(f"{line_number}\t{match.group(0)}", file=origin_out)
