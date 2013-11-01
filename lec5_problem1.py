def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    #if exp == 0:
    #    return 1
    #else:
    #    result = base

    # - solution match shorter:
    
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
        
            
