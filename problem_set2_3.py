def lowest_payment(balance, annualInterestRate):
    payment = 10
    monthlyInterestRate = annualInterestRate /12.0
    balancePaid = balance
    
    while (balancePaid >= 0):
        balancePaid = balance        
        payment += 10
        totalPaid = 0.0    
        for month in range(1,13):            
            balancePaid -= payment
            balancePaid += balancePaid * monthlyInterestRate
            month += 1

    print('Lowest Payment: ' + str(payment))

