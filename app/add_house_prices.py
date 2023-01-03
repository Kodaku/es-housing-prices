import pandas as pd
from elasticsearch import Elasticsearch
from add_data import add_data
from create_es_index import es_create_index_if_not_exists


es = Elasticsearch(
    hosts=['http://host.docker.internal:9200'],
    basic_auth=('elastic', 'e0_kX+xT1Oh_v+8pLot3')
)

data_types = {}

prices = pd.read_csv("./app/train.csv")

for data_type, column in zip(prices.dtypes, prices.columns):
    data_types[column] = str(data_type)

print(data_types)

if es.indices.exists(index="house_prices"):
    add_data(es, prices, data_types)
else:
    es_create_index_if_not_exists(elastic_instance=es, created_index="house_prices")
    add_data(es=es, prices=prices, data_types=data_types)
