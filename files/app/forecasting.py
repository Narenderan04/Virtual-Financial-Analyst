import pandas as pd

class Forecasting:
    def __init__(self, data):
        self.data = data

    def rolling_forecast(self, window=5):
        self.data['Rolling Mean'] = self.data['Close'].rolling(window=window).mean()
        self.data['Rolling Std'] = self.data['Close'].rolling(window=window).std()
        return self.data