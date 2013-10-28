def lowest_payment(balance, annualInterestRate):
    
    def annualy(balance, monthlyInterestRate, lowestPayment):
        totalPaid = 0.0    
        for month in range(1,13):            
            balance -= lowestPayment
            interest = balance * monthlyInterestRate
            balance += interest
            totalPaid += lowestPayment
            #print('Month: ' + str(month))
            #print('Ramaining balance: ' + str(round(balance, 2)))
            month += 1
        #print('Total paid: ' + str(round(totalPaid, 2)))
        return totalPaid
    
    lowestPayment = 10
    monthlyInterestRate = annualInterestRate /12.0
    totalPaid = 0.0
    while (balance - totalPaid) >= 0:
        totalPaid = annualy(balance, monthlyInterestRate, lowestPayment)
        lowestPayment += 10
 
    print('Ramaining balance: ' + str(round(balance, 2)))
    print('Lowest Payment: ' + str(lowestPayment))

