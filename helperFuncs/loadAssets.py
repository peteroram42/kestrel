import json

def load_coins(filename):
  with open(filename, "r") as f:
    try:
      data = json.load(f)
      coinData = data['coins']
      coinString = ','.join(map(str, coinData))
      return coinString
    except json.JSONDecodeError as e:
      print(f"Error parsing watchedAssets.json: {e}")
      return None

def load_stocks(filename):
    return False;