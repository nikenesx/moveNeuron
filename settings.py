from typing import Union

# Строка, с которой начинаются векторы значения во входных файлах с данными
# (изменять только в случае изменения формата входных данных).
DATA_VECTORS_START_LINE: int = 7


# Количество датчиков, которое используется для обучения сети.
SENSORS_COUNT: int = 4


WINDOW_SIZE: float = 0.2


# Директория с входными данными.
DATASET_PATH: str = 'dataset2'


TRAIN_MODEL_OPTIONS: dict[str, Union[int, float]] = {
    # Размер батча. Определяет, через какое кол-во прогона входных векторов будут корректироваться веса.
    # Позволяет быстрее обучаться сети.
    # Возможные значения: от 0 до 10.000
    # Рекомендованные значения: от 10 до 1.000
    'batch_size': 10,

    # Количество эпох обучения. Определяет, сколько раз будут прогоняться входные данные. Подача всех векторов на вход
    # для обучения один раз = 1 эпоха.
    # Возможные значения: от 1 до ∞
    'epochs_count': 1000,

    # Размер выборки валидации. Определяет, какой процент от входных данных будет использоваться для выборки валидации
    # (необходимо для предотвращения переобучения модели).
    # Возможные значения: от 0.0 до 1.0
    # Рекомендованные значения: от 0.1 до 0.3
    'validation_split': 0.05,
}


MODEL_NAME: str = 'move_types_model.h5'
