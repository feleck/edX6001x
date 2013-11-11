def test():
    print laceStringsRecur('', '') == ''
    print laceStringsRecur('', 'abc') == 'abc'
    print laceStringsRecur('abc', '') == 'abc'
    print laceStringsRecur('abc', 'def') == 'adbecf'
    print laceStringsRecur('abc', 'defgh') == 'adbecfgh'
    print laceStringsRecur('abcd', 'ef') == 'aebfcd'

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            print s1
            print s1[:-1]
            return s1[0]+s2[0]+helpLaceStrings(s1[1:], s2[1:], '')
    return helpLaceStrings(s1, s2, '')
    

# from previous problem:

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    '''
    if s1 == '':
        return s2
    if s2 == '':
        return s1
    '''
    def equal(len_e, s1, s2):
        i = 0
        result = ''
        while i < len_e:
            result += s1[i]+s2[i]
            i+=1
        return result

    len1 = len(s1)
    len2 = len(s2)
    if len1 == len2:
        return equal(len1, s1, s2)
    elif len1 > len2:
        return equal(len2, s1[:len2], s2) + s1[len2:]
    else:
        return equal(len1, s1, s2[:len1]) + s2[len1:]
