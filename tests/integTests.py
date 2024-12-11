# integ tests

from clients.cmc.cmcClient import CoinMarketCapClient

def run_integ_tests(mode):
    if cmc_integ_test(mode):
        return True
    else:
        return False

def cmc_integ_test(mode):
    cmcClient = CoinMarketCapClient()
    params = {"amount": 1, "id": 1, "convert": "ETH"}
    data_json = cmcClient.do_price_conversion(params)
    if data_json["data"]["quote"]["ETH"]["price"] > 1:
        if mode == "debug":
            print("cmcClient - integ: pass")
        return True
    else:
        if mode == "debug":
            print("cmcClient - integ: failure")
        return False