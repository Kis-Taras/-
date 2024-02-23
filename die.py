import random

def throw_dice(N: int) -> tuple[int, int]:
    """
    Симулює кидання двох кубиків з N гранями кожен.
    """
    dice1 = random.randint(1, N)
    dice2 = random.randint(1, N)
    return dice1, dice2

def symmetric_simulation(N: int, trials: int) -> dict[int, int]:
    """
    Проводить симуляцію з симетричними кубиками.
    """
    results = {}
    for _ in range(trials):
        dice1, dice2 = throw_dice(N)
        total = dice1 + dice2
        results[total] = results.get(total, 0) + 1
    return results

def asymmetric_simulation(N: int, trials: int) -> dict[int, int]:
    """
    Проводить симуляцію з асиметричними кубиками.
    """
    results = {}
    for _ in range(trials):
        dice1 = random.randint(1, N)
        dice2 = random.randint(1, N)
        total = dice1 + dice2
        results[total] = results.get(total, 0) + 1
    return results

def main():
    N = 18
    trials = 10000

    # Симуляція з симетричними кубиками
    symmetric_results = symmetric_simulation(N, trials)
    print("Результати симуляції з симетричними кубиками:")
    for outcome, count in symmetric_results.items():
        print(f"Сума {outcome}: {count} випадань")

    # Симуляція з асиметричними кубиками
    asymmetric_results = asymmetric_simulation(N, trials)
    print("\nРезультати симуляції з асиметричними кубиками:")
    for outcome, count in asymmetric_results.items():
        print(f"Сума {outcome}: {count} випадань")

if __name__ == "__main__":
    main()
