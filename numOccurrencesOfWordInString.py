'''
find number of ways have a substring inside a string

be careful! This isn't as simple as s.count(sub_str)
since if have multiple places can appear with overlap, then count twice!

assume sub_str is not empty
'''

def numPossibleOccurrences(s, sub_str):
    '''
    >>> numPossibleOccurrences("abc", "a")
    1
    >>> numPossibleOccurrences("abc", "c")
    1
    >>> numPossibleOccurrences("", "a")
    0
    >>> numPossibleOccurrences("aaa", "a")
    3
    >>> numPossibleOccurrences("aaa", "aa")
    2
    >>> numPossibleOccurrences("aaa", "aaa")
    1
    '''
    # TODO = fill in this function, and return correct result
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
