# unit tests

from helperFuncs.loadAssets import load_coins
from clients.cmc.cmcClient import CoinMarketCapClient

def run_unit_tests(mode):
    if load_coins_unit_test(mode) and cmcClient_unit_test(mode):
        return True
    else: 
        return False

def load_coins_unit_test(mode):
    coinString = load_coins("watchedAssets.json")
    if isinstance(coinString, str) and len(coinString) > 2:
        if mode == "debug":
            print("load_coins - unit: pass")
        return True
    else:
        if mode == "debug":
            print("load_coins - unit: failure")
        return False

def cmcClient_unit_test(mode):
    cmcClient = CoinMarketCapClient()
    if len(cmcClient.api_key) == 36:
        if mode == "debug":
            print("cmcClient - unit: pass")
        return True
    else:
        if mode == "debug":
            print("cmcClient - unit: failure")
        return False
