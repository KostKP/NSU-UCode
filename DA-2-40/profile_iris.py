from sklearn.datasets import load_iris
import pandas as pd
from ydata_profiling import ProfileReport


def main():
    # === 1. Загружаем датасет === #
    iris = load_iris(as_frame=True)
    df = iris.frame  # уже готовый pandas DataFrame

    # === 2. Создаём профильный отчёт === #
    profile = ProfileReport(
        df,
        title="📊 Отчёт по Iris Dataset",
        explorative=True
    )

    # === 3. Сохраняем отчёт в HTML === #
    output_file = "iris_report.html"
    profile.to_file(output_file)

    print(f"[✔] Отчёт успешно сохранён: {output_file}")


if __name__ == "__main__":
    main()
