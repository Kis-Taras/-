import random  # Імпорт модуля random для генерації випадкових чисел.

def throw_dice(N: int) -> tuple[int, int]:
    """
    Симулює кидання двох кубиків з N гранями кожен.
    """
    # Генерує випадкові числа від 1 до N для обох кубиків.
    dice1 = random.randint(1, N)
    dice2 = random.randint(1, N)
    return dice1, dice2

def symmetric_simulation(N: int, trials: int) -> dict[int, int]:
    """
    Виконує симуляцію з симетричними кубиками.
    """
    results = {}  # Словник для зберігання кількості випадків для кожної суми чисел на кубиках.
    for _ in range(trials):
        # Кидає два кубики та обчислює їх суму.
        dice1, dice2 = throw_dice(N)
        total = dice1 + dice2
        results[total] = results.get(total, 0) + 1
    return results

def asymmetric_simulation(N: int, trials: int) -> dict[int, int]:
    """
    Виконує симуляцію з асиметричними кубиками.
    """
    results = {}  # Словник для зберігання кількості випадків для кожної суми чисел на кубиках.
    for _ in range(trials):
        # Кидає два кубики, один із яких асиметричний, та обчислює їх суму.
        dice1 = random.randint(1, N)
        dice2 = random.randint(1, N)
        total = dice1 + dice2
        results[total] = results.get(total, 0) + 1
    return results

def main():
    N = 15  # Кількість граней кожного кубика.
    trials = 10000  # Кількість експериментів (кидань кубиків).

    # Симуляція з симетричними кубиками
    symmetric_results = symmetric_simulation(N, trials)
    print("Результати симуляції з симетричними кубиками:")
    for outcome, count in symmetric_results.items():
        print(f"Всього {outcome}: {count} випадків")

    # Симуляція з асиметричними кубиками
    asymmetric_results = asymmetric_simulation(N, trials)
    print("\nРезультати симуляції з асиметричними кубиками:")
    for outcome, count in asymmetric_results.items():
        print(f"Всього {outcome}: {count} випадків")

if __name__ == "__main__":
    main()
