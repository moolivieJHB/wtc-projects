print('[Module] online.Reconciliation loaded.')
'''Outputs that the online.Reconciliation has been loaded.'''
import requests
def do_reconciliation():
    '''This function outputs that the Online Bank reconciliation is being done
     and it alsomakes a request and prints the response'''
    print('Doing Online Bank reconciliation.')
    response = requests.get('https://www.wethinkcode.co.za')
    print(response.status_code)
# if you print(response.text) you will see the actual WeThinkCode_ website HTML content
