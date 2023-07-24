"""
I am working on a problem that simply calculates and prints the credit card balance. I hope this code can be improved/optimized a lot.

I am from a Java background. If it was Java code, I would have pulled all the code lines inside the for loop and place it at the beginning of the method and inside for loop I would call the method recursively. I tried to do the same in python but it hit me with some error:

RuntimeError: maximum recursion depth exceeded while calling a Python object

From a quick internet search I found that it is better to go for iteration instead of recursion:
"""
'''
Program to calculate credit card balance after 1 year
'''
def calculateCreditCardBalance(balance, annualInterestRate, monthlyPaymentRate):

    totalPaid = 0

    for thisMonth in range(1,13):
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = round(monthlyPaymentRate * balance, 2)
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        updatedBalanceEachMonth = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance) , 2) 
        print ('Month: %d' %(thisMonth))
        print ('Minimum monthly payment: ' + str(minimumMonthlyPayment))
        print ('Remaining balance: ' + str(updatedBalanceEachMonth))

        balance = updatedBalanceEachMonth
        totalPaid += minimumMonthlyPayment

    print ('Total paid: ' + str(totalPaid))
    print ('Remaining balance: '+ str(balance))


calculateCreditCardBalance(4842, 0.2, 0.04)

def credit_card_balance(balance, interest_rate, payment_rate, verbose=False):
    '''Return credit card balance after 1 year'''
    total = 0
    interest_rate /= 12.0
    for month in range(12):
        minimum_payment = round(payment_rate * balance, 2)
        total += minimum_payment
        balance = round((1 + interest_rate) * (balance - minimum_payment), 2)
        if verbose:
            print ("""Month: {}
Minimum monthly payment: {}
Remaining balance: {}
""".format(month+1, minimum_payment, balance))

    if verbose:
        print ('Total paid: {}'.format(total))
    return balance

if __name__ == "__main__":
    balance = 4842
    balance = credit_card_balance(balance, 0.2, 0.04, True)
    