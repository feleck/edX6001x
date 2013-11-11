test = ('I', 'am', 'a', 'test', 'tuple')
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result = ()
    i =  0
    while i < len(aTup):
        if i % 2 == 0:
            result += (aTup[i:i+1])
        i+= 1
        #print result
    return result


# Solution from page:
def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    return aTup[::2]
