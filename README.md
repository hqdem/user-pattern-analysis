## Структура папок

```
├───data  # папка с датасетами
│   └───lmsys-chat-1m
│       │   train-00000-of-00006-4feeb3f83346a0e9.parquet # датасет для обучения и обработки. скачать можно [тут](https://huggingface.co/datasets/lmsys/lmsys-chat-1m/blob/main/data/train-00000-of-00006-4feeb3f83346a0e9.parquet).
│       │
│       └───processed # папка с генерированными и обработанными файлами
│               dialogs.csv             # обработанный изначальный датасет
│               features.csv            # метки для кластеризации 
│               features_normalized.csv # нормализованные метки для кластеризации
│               kmeans_clusters.csv     # результаты кластеризации Kmeans (метки + user_id + кластера)
│
├───models # папка с экспортом моделей
│   ├───gradient_boosting # gradient boosting модели
│   │       model_lightgbm.pkl
│   │       model_lightgbm_wo_duplicates.pkl
│   │       model_xgboost.pkl
│   │       model_xgboost_wo_duplicates.pkl
│   │
│   ├───logistic_regression  # logistic regression модели
│   │       model.pkl
│   │       model_wo_duplicates.pkl
│   │
│   └───random_forest  # random forest модели
│           model.pkl
│           model_wo_duplicates.pkl
│
└───src # папка с исходным кодом
    ├───chatcluster # код устанавливаемой библиотеки
    │   │   main.py
    │   │   preprocessor.py
    │   │   __init__.py
    │   │
    │   └───models # те же модели для устанавливаемой библиотеки
    │       ├───gradient_boosting
    │       │       model_lightgbm.pkl
    │       │       model_lightgbm_wo_duplicates.pkl
    │       │       model_xgboost.pkl
    │       │       model_xgboost_wo_duplicates.pkl
    │       │
    │       ├───logistic_regression
    │       │       model.pkl
    │       │       model_wo_duplicates.pkl
    │       │
    │       └───random_forest
    │               model.pkl
    │               model_wo_duplicates.pkl
    │
    ├───classification  # папка с алгоритмами классификации
    │   ├───gradient_boosting  # gradient boosting
    │   │       lightgbm.ipynb # lightgbm
    │   │       xgboost.ipynb  # xgboost
    │   │
    │   ├───logistic_regression # logistic regression
    │   │       logistic_regression.ipynb # logistic regression
    │   │
    │   └───random_forest # random forest
    │           random_forest.ipynb # random forest
    │
    ├───clusterization  # папка с алгоритмами кластеризации
    │   ├───dbscan  # кластеризация для DBSCAN
    │   │       dbscan.ipynb # реализация кластеризации для DBSCAN
    │   │
    │   ├───hdbscan # кластеризация для HDBSCAN
    │   │       hdbscan.ipynb # реализация кластеризации для HDBSCAN
    │   │
    │   ├───hierarchy # иерархическая кластеризация
    │   │       hierarchy.ipynb # реализация иерархической кластеризации
    │   │
    │   └───kmeans # кластеризация для Kmeans
    │           kmeans.ipynb # реализация кластеризации для Kmeans 
    │           kmeans_results_visualizing.ipynb # анализ и визуализация результатов кластеризации Kmeans
    │
    └───preprocessing # предварительная обработка сырого датасета
            preprocessing.ipynb # реализация предварительной обработки сырого датасета
```

## Установка библиотеки

1) Склонировать репозиторий - `git clone https://github.com/hqdem/user-pattern-analysis.git`
2) С активированным виртуальным окружением выполнить команду `pip install <путь до клонированного репозитория>`
3) Все готово к использованию. Слонированный репозиторий можно удалить.

## Пример использования
```python
from chatcluster import predict_user_pattern

if __name__ == '__main__':
    pattern = predict_user_pattern(["hello can you explain me generics in go?", "wow, that's insane, thanks!"])
    print(f'user pattern is {pattern}')
```
