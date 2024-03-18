from dataloader.coinbaseloader import CoinbaseLoader, Granularity
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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
    #ax1.title('Аналіз ціни BTC')
    #ax1.xlabel('Дата')
    #ax1.ylabel('Ціна закриття')
    #ax1.legend()
    ax1.grid()

    ax2.plot(df_2.close, label='Ціна закриття')
    ax2.plot(df_2.SMA20, label='SMA 20 днів')
    ax2.plot(df_2.SMA50, label='SMA 50 днів')
    ax2.grid()

    ax3.plot(df_3.close, label='Ціна закриття')
    ax3.plot(df_3.SMA20, label='SMA 20 днів')
    ax3.plot(df_3.SMA50, label='SMA 50 днів')
    ax3.grid()

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