# Импорт необходимых библиотек
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def prepare_data():
    # Загрузка данных с правильным указанием заголовков
    data = pd.read_csv('data/raw/data.csv', header=0)

    # Проверка загруженных данных
    print("data:")
    print(data.head())

    # Базовая очистка (например, удаление NaN)
    data.dropna(inplace=True)

    # Проверка после очистки
    print("data")
    print(data.head())
    print(f"string: {len(data)}")

    # Сплит на train и test
    if len(data) == 0:
        raise ValueError("error")

    train, test = train_test_split(data, test_size=0.2, random_state=42)

    # Создание директории, если она не существует
    os.makedirs('data/processed', exist_ok=True)

    # Сохранение обработанных данных
    train.to_csv('data/processed/train.csv', index=False)
    test.to_csv('data/processed/test.csv', index=False)

# Вызов функции для подготовки данных
if __name__ == "__main__":
    prepare_data()



