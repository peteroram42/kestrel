'''
    verif all ok or fail
DONE get update of what we need to get
    create list of alerts
    send notifications
'''

from tests.runTests import run_all_tests
from getCoinUpdate import get_coin_update

if run_all_tests():

    data = get_coin_update()

    if data:
        print(data)

else:
    run_all_tests("debug")
