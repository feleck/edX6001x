def paying_minimum(balance, annualInterestRate, monthlyPaymentRate):
    minimumMonthlyPayment=0.0
    totalPaid = 0.0

    for month in range(1,13):
        minimumMonthlyPayment = balance * monthlyPaymentRate
        balance -= minimumMonthlyPayment
        monthlyInterestRate = annualInterestRate /12.0
        interest = balance * monthlyInterestRate
        balance += interest
        totalPaid += minimumMonthlyPayment
        print('Month: ' + str(month))
        print('Minimum monthly payment: ' + str(round(minimumMonthlyPayment, 2)))
        print('Ramaining balance: ' + str(round(balance, 2)))
        month += 1
    print('Total paid: ' + str(round(totalPaid, 2)))
    print('Ramaining balance: ' + str(round(balance, 2)))
