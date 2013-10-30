def lowest_payment2(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate /12.0
    paymentLower = balance/12.0
    paymentUpper = (balance * (1 + monthlyInterestRate)**12)/12.0
    balancePaid = balance
    payment = (paymentLower+paymentUpper)/2.0
    
    while (abs(balancePaid) >= 0.01):
        balancePaid = balance
        for month in range(1,13):
            balancePaid -= payment
            balancePaid += balancePaid * monthlyInterestRate
            month += 1

        if balancePaid <= 0:
            paymentUpper = payment
            payment = (paymentLower+paymentUpper)/2.0
        else:
            paymentLower = payment
            payment = (paymentLower+paymentUpper)/2.0
        
    print('Lowest Payment: ' + str(round(payment, 2)))

