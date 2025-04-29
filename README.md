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
└───src # папка с исходным кодом
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
