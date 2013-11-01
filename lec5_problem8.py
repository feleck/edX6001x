def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    middle = len(aStr)/2
    if aStr == '':
        return False
    elif char == aStr[middle]:
        return True
    if char > aStr[middle]:
        return isIn(char, aStr[middle + 1:])
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle])
#    return False
