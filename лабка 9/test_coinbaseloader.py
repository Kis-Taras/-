import pytest
from dataloader.coinbaseloader import CoinbaseLoader, Granularity
from models.historical_data import HistoricalData
from pydantic import ValidationError
from typing import Literal
import asyncio
import json
import os

@pytest.fixture
async def loader():
    return CoinbaseLoader()

@pytest.mark.asyncio
async def test_get_pairs(loader):
    pairs = await loader.get_pairs()
    assert isinstance(pairs, list), "get_pairs повинен повертати список"
    assert pairs, "Список не повинен бути порожнім"

@pytest.mark.asyncio
@pytest.mark.parametrize("pair", ["BTC-USDT", "ETH-USDT"])
async def test_get_stats(loader, pair: Literal['BTC-USDT'] | Literal['ETH-USDT']):
    stats = await loader.get_stats(pair)
    assert isinstance(stats, dict), "get_stats повинен повертати словник"
    assert stats, "Словник не повинен бути порожнім"

@pytest.mark.asyncio
@pytest.mark.parametrize("pair, begin, end, granularity", [("BTC-USDT", "2023-01-01", "2023-06-30", Granularity.ONE_DAY)])
async def test_get_historical_data(loader, pair: Literal['BTC-USDT'], begin: Literal['2023-01-01'], end: Literal['2023-06-30'], granularity: Granularity):
    data = await loader.get_historical_data(pair, begin, end, granularity)
    assert isinstance(data, list), "get_historical_data повинен повертати список"
    assert data, "Список не повинен бути порожнім"

    # Перевірка валідації моделі Pydantic
    try:
        HistoricalData(pair=pair, begin=begin, end=end, granularity=granularity, data=data)
    except ValidationError as e:
        # Якщо дані не валідні, збережемо їх у JSON-файл
        invalid_data_filename = f"invalid_data_{pair}_{begin}_{end}_{granularity}.json"
        with open(invalid_data_filename, 'w') as f:
            json.dump(data, f, indent=4)
        raise AssertionError(f"Дані не валідні. Збережено у файлі: {invalid_data_filename}") from e
    
    # Зберегти валідні дані у JSON-файл
    valid_data_filename = f"valid_data_{pair}_{begin}_{end}_{granularity}.json"
    with open(valid_data_filename, 'w') as f:
        json.dump(data, f, indent=4)

    # Перевірка, чи файли існують
    assert os.path.isfile(valid_data_filename), "Файл з валідними даними не знайдено"
    assert os.path.isfile(invalid_data_filename), "Файл з невалідними даними не знайдено"

    # Видалення файлів після тесту
    os.remove(valid_data_filename)
    os.remove(invalid_data_filename)
