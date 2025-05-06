import requests

class APIIntegration:
    def __init__(self, api_key):
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = api_key

    def fetch_time_series_data(self, symbol, interval="daily"):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("API request failed with status code: {}".format(response.status_code))