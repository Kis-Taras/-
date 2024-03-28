from dataloader.coinbaseloader import CoinbaseLoader, Granularity
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime, timedelta

def get_half_year_data(loader, symbol, year, first_half):
    # Встановлюємо початкову дату
    start_date = datetime(year, 1 if first_half else 7, 1)
    # Встановлюємо кінцеву дату
    end_date = datetime(year, 6 if first_half else 12, 30 if first_half else 31)
    
    # Отримуємо історичні дані за піврік
    data = loader.get_historical_data(symbol, start_date, end_date, Granularity.ONE_DAY)
    
    return data

def main():
    loader = CoinbaseLoader()

    # Отримуємо дані за першу половину року для кожного з обраних продуктів
    df_1_first_half = get_half_year_data(loader, "btc-usdt", 2023, True)
    df_2_first_half = get_half_year_data(loader, "gmt-usdt", 2023, True)
    df_3_first_half = get_half_year_data(loader, "eth-usdt", 2023, True)

    # Отримуємо дані за другу половину року для кожного з обраних продуктів
    df_1_second_half = get_half_year_data(loader, "btc-usdt", 2023, False)
    df_2_second_half = get_half_year_data(loader, "gmt-usdt", 2023, False)
    df_3_second_half = get_half_year_data(loader, "eth-usdt", 2023, False)

    # Об'єднуємо дані за півроку для кожного продукту
    df_1 = pd.concat([df_1_first_half, df_1_second_half])
    df_2 = pd.concat([df_2_first_half, df_2_second_half])
    df_3 = pd.concat([df_3_first_half, df_3_second_half])

    # Проводимо аналіз та будуємо графіки
    # do some analysis
    df_1['SMA20'] = df_1['close'].rolling(window=20).mean()
    df_1['SMA50'] = df_1['close'].rolling(window=50).mean()
    
    df_2['SMA20'] = df_2['close'].rolling(window=20).mean()
    df_2['SMA50'] = df_2['close'].rolling(window=50).mean()

    df_3['SMA20'] = df_3['close'].rolling(window=20).mean()
    df_3['SMA50'] = df_3['close'].rolling(window=50).mean()

    # Побудова графіків
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 7))

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

    plt.legend()
    plt.show()

    # Побудова теплової карти для кореляції
    df = pd.merge(df_1, pd.merge(df_2, df_3, left_index=True, right_index=True), left_index=True, right_index=True)
    cm = df[['close_x', 'close_y']].corr()
    sns.heatmap(cm, annot=True)
    plt.show()

    # Обчислення і виведення волатильності
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