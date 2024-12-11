# CoinMarketCap Client

import os
import requests
from dotenv import load_dotenv
from .cmcEndpoints import endpoints

load_dotenv()

class CoinMarketCapClient:
    def __init__(self):
        self.api_key = os.getenv('CMC_API_KEY')
        self.endpoint = ""
        self.headers = []
        self.params = {}

    def fetch_data(self, endpoint, params=None):
        headers = {
            'Accept': 'applicaton/json',
            'X-CMC_PRO_API_KEY': self.api_key
        }

        try:
            response = requests.get(f"{endpoint}", params=params, headers=headers)
            response.raise_for_status()
            return response.json()  

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None  

    def get_crypto_prices(self, params):
        endpoint = endpoints["latestQuotes"]
        return self.fetch_data(endpoint, params)

    def get_coin_map(self):
        endpoint = endpoints["idMap"]
        return self.fetch_data(endpoint)
    
    def do_price_conversion(self, params):
        endpoint = endpoints["priceConversion"]
        return self.fetch_data(endpoint, params)