import json

from helperFuncs.loadAssets import load_coins
from clients.cmc.cmcClient import CoinMarketCapClient


def get_coin_update():

    coins = load_coins("watchedAssets.json")

    cmcClient = CoinMarketCapClient()

    data = cmcClient.get_crypto_prices({'id': coins})

    if data:
        return json.dumps(data, indent=4)

