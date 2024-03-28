import json
import pandas as pd
from datetime import datetime
from enum import Enum
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class BaseDataLoader:
    def __init__(self, endpoint=None):
        self._base_url = endpoint

    def _get_req(self, resource, params=None):
        req_url = self._base_url + resource
        if params is not None:
            response = requests.get(req_url, params=params)
        else:
            response = requests.get(req_url)
        if response.status_code != 200:
            msg = f"Unable to request data from {req_url}, status: {response.status_code}"
            if response.text and response.text.message:
                msg += f", message: {response.text.message}"
            raise RuntimeError(msg)
        return response.text

class Granularity(Enum):
    ONE_MINUTE = 60
    FIVE_MINUTES = 300
    FIFTEEN_MINUTES = 900
    ONE_HOUR = 3600
    THREE_HOUR = 10800
    SIX_HOURS = 21600
    ONE_DAY = 86400

class CoinbaseLoader(BaseDataLoader):
    def __init__(self, endpoint="https://api.exchange.coinbase.com"):
        super().__init__(endpoint)

    def get_pairs(self) -> pd.DataFrame:
        data = self._get_req("/products")
        df = pd.DataFrame(json.loads(data))
        df.set_index('id', drop=True, inplace=True)
        return df

    def get_stats(self, pair: str) -> pd.DataFrame:
        data = self._get_req(f"/products/{pair}")
        return pd.DataFrame(json.loads(data), index=[0])

    def get_historical_data(self, pair: str, begin: str, end: str, granularity: Granularity) -> pd.DataFrame:
        params = {
            "start": begin,
            "end": end,
            "granularity": granularity.value
        }
        # retrieve needed data from Coinbase
        data = self._get_req(f"/products/{pair}/candles", params)
        if data:
            df = pd.DataFrame(data, columns=("timestamp", "low", "high", "open", "close", "volume"))
            # Convert timestamp to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
            # use timestamp column as index
            df.set_index('timestamp', drop=True, inplace=True)
            return df
        else:
            print("No data received from the API.")
            return pd.DataFrame()

def main():
    loader = CoinbaseLoader()
    df_1 = loader.get_historical_data("btc-usdt", "2023-01-01", "2023-01-02", Granularity.FIVE_MINUTES)
    df_2 = loader.get_historical_data("gmt-usdt", "2023-01-01", "2023-01-02", Granularity.FIVE_MINUTES)
    df_3 = loader.get_historical_data("eth-usdt", "2023-01-01", "2023-01-02", Granularity.FIVE_MINUTES)

    # do some analysis
    df_1['SMA20'] = df_1['close'].rolling(window=20).mean()
    df_1['SMA50'] = df_1['close'].rolling(window=50).mean()
    
    df_2['SMA20'] = df_2['close'].rolling(window=20).mean()
    df_2['SMA50'] = df_2['close'].rolling(window=50).mean()

    df_3['SMA20'] = df_3['close'].rolling(window=20).mean()
    df_3['SMA50'] = df_3['close'].rolling(window=50).mean()

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig.set_figwidth(14)
    fig.set_figheight(7)

    ax1.plot(df_1.close, label='Ціна закриття')
    ax1.plot(df_1.SMA20, label='SMA 20 днів')
    ax1.plot(df_1.SMA50, label='SMA 50 днів')
    ax1.grid()

    ax2.plot(df_2.close, label='Ціна закриття')
    ax2.plot(df_2.SMA20, label='SMA 20 днів')
    ax2.plot(df_2.SMA50, label='SMA 50 днів')
    ax2.grid()

    ax3.plot(df_3.close, label='Ціна закриття')
    ax3.plot(df_3.SMA20, label='SMA 20 днів')
    ax3.plot(df_3.SMA50, label='SMA 50 днів')
    ax3.grid()

    plt.tight_layout()
    plt.show()

    df = pd.merge(df_1, pd.merge(df_2, df_3, left_index=True, right_index=True), left_index=True, right_index=True)
    cm = df[['close_x', 'close_y']].corr()
    sns.heatmap(cm, annot=True)
    plt.show()

    df_1['LR'] = np.log(df_1.close/df_1.close.shift(1))
    plt.plot(df_1.LR)
    plt.grid()
    plt.show()
    print(f"volatility: {df_1.LR.std():0.4f}")

    df_2['LR'] = np.log(df_2.close/df_2.close.shift(1))
    plt.plot(df_2.LR)
    plt.grid()
    plt.show()
    print(f"volatility: {df_2.LR.std():0.4f}")

    df_3['LR'] = np.log(df_3.close/df_3.close.shift(1))
    plt.plot(df_3.LR)
    plt.grid()
    plt.show()
    print(f"volatility: {df_3.LR.std():0.4f}")

if __name__ == "__main__":
    main()
