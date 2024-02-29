import plotly.graph_objs as go
from plotly.subplots import make_subplots
import random
import webbrowser

def simulate_dice_roll(N: int, symmetric: bool, trials: int) -> dict[int, int]:
    """
    Симулює кидання двох гральних кубиків з N гранями.
    """
    results = {}
    for _ in range(trials):
        if symmetric:
            dice1 = random.randint(1, N)
            dice2 = random.randint(1, N)
        else:
            dice1 = random.randint(1, N)
            dice2 = random.randint(1, dice1)
        total = dice1 + dice2
        results[total] = results.get(total, 0) + 1
    return results

def main():
    N = 15 + 3  # Кількість граней кубика
    trials = 10000  # Кількість симуляцій

    # Симуляція для обох варіантів
    symmetric_results = simulate_dice_roll(N, symmetric=True, trials=trials)
    asymmetric_results = simulate_dice_roll(N, symmetric=False, trials=trials)

    # Побудова гістограми
    fig = make_subplots(rows=2, cols=1, subplot_titles=("Симетричний кубик", "Асиметричний кубик"))

    fig.add_trace(go.Bar(x=list(symmetric_results.keys()), y=list(symmetric_results.values()), name="Симетричний кубик"), row=1, col=1)
    fig.add_trace(go.Bar(x=list(asymmetric_results.keys()), y=list(asymmetric_results.values()), name="Асиметричний кубик"), row=2, col=1)

    fig.update_layout(title_text="Гістограма сум результатів кидання двох кубиків",
                      xaxis_title="Сума результатів",
                      yaxis_title="Кількість випадків")

    fig.write_html("histogram.html")  # Зберігає гістограму у вигляді HTML-файлу

    # Відкриття гістограми у браузері
    webbrowser.open('histogram.html')

if __name__ == "__main__":
    main()
