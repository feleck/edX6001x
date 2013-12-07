def genPrimes2():
    i = 0
    while True:
        next = i
        yield next
        i += 1

def genPrimes():
    x = 2
    primes = []
   
    while True:
        test = 1
        next = x

        for p in primes:
            if (x % p) != 0:
                test *= 1
            else:
                test *= 0
        if test == 1:
            primes.append(x)
            x += 1
            yield next
        else:
            x += 1

# course solution:

def genPrimes3():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last        
        
        

gen = genPrimes()
#gen2 = genPrimes2()
