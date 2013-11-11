def test():
    print McNuggets(0) == False
    print McNuggets(5) == False
    print McNuggets(6) == True
    print McNuggets(7) == False
    print McNuggets(8) == False
    print McNuggets(9) == True
    print McNuggets(10) == False
    print McNuggets(12) == True
    print McNuggets(15) == True
    print McNuggets(18) == True
    print McNuggets(19) == False
    print McNuggets(20) == True
    print McNuggets(21) == True
    print McNuggets(26) == True
    print McNuggets(29) == True
    print McNuggets(35) == True
    print McNuggets(40) == True
    
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a, b ,c = 0, 0, 0
    sol = False
    def calc(a, b, c):
        return 6*a + 9*b + 20*c
    
    while a < n:
        b = 0
        while b < n:
            c = 0
            while c < n:
                if calc(a, b, c) == n:
                    return True
                c += 1
            b += 1
        a += 1
    return sol
