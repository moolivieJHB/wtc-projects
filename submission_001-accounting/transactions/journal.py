print('[Module] Journal loaded.')
'''Prints that the journal has been loaded'''
def receive_income(amount):
    '''This function prints the amount of income recieved too 2 decimal places.'''
    amount=float(amount)
    amount= "{:.2f}".format(amount)

    print("[Journal] Received R" + str(amount))

def pay_expense(amount):
    '''This function prints the amount of income paid too 2 decimal places'''
    amount= "{:.2f}".format(amount)
    print('[Journal] Paid R' + str(amount))
