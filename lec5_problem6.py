def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # my solution: RECURSIVE!!!! - should be iterative
    '''
    if aStr == '':
        return 0
    else:
        return 1 + lenIter(aStr[:-1])
    '''
    length = 0
    while aStr != '':
        aStr = aStr[:-1]
        length  += 1
    return length
