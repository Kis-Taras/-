import pytest
from dataloader.coinbaseloader import CoinbaseLoader
from models import Pairs
import json

@pytest.fixture
def loader():
    return CoinbaseLoader()

def test_pairs_model_validation():
    # Завантажуємо тестові дані з JSON-файлу
    with open("valid_pairs.json", "r") as f:
        valid_data = json.load(f)
    with open("invalid_pairs.json", "r") as f:
        invalid_data = json.load(f)
    
    # Перевіряємо валідні дані
    for data in valid_data:
        pairs = Pairs(**data)
        assert pairs

    # Перевіряємо невалідні дані
    for data in invalid_data:
        with pytest.raises(ValueError):
            Pairs(**data)

def test_get_pairs_with_valid_data(loader):
    # Завантажуємо тестові дані з JSON-файлу
    with open("valid_pairs.json", "r") as f:
        valid_data = json.load(f)

    # Викликаємо функцію get_pairs для кожного валідного набору даних
    for data in valid_data:
        pairs = Pairs(**data)
        result = loader.get_pairs()
        assert pairs in result

def test_get_pairs_with_invalid_data(loader):
    # Завантажуємо тестові дані з JSON-файлу
    with open("invalid_pairs.json", "r") as f:
        invalid_data = json.load(f)

    # Викликаємо функцію get_pairs для кожного невалідного набору даних
    for data in invalid_data:
        with pytest.raises(ValueError):
            Pairs(**data)
            loader.get_pairs()

