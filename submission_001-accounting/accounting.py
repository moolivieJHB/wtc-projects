#import user.authentication
''' import the packages '''
import user.authentication
import transactions.journal
#import banking.reconciliation
#import banking.fvb.reconciliation
#import banking.ubsa.reconciliation
import sys
import requests
#import banking.online.reconciliation
import banking

if __name__ == "__main__":
    '''main function implements other fuctions 
    and print out the arguments parsed during runtime.
    '''
    if len(sys.argv)>1:
        for i in range(len(sys.argv)):
            print(sys.argv[i] )
    #help("modules")

    (user.authentication.authenticate_user())
    (transactions.journal.receive_income(100))
    (transactions.journal.pay_expense(100))
    #(banking.reconciliation.do_reconciliation())
    (banking.fvb.reconciliation.do_reconciliation())
    #(banking.ubsa.reconciliation.do_reconciliation())
    #(banking.online.reconciliation.do_reconciliation())

    # receive_income(100.00)
    # pay_expense(100.00)