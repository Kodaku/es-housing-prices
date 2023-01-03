import os

import pandas as pd
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    hosts=['http://host.docker.internal:9200'],
    basic_auth=('elastic', 'e0_kX+xT1Oh_v+8pLot3')
)

data_types = {}

prices = pd.read_csv("./app/train.csv")

for data_type, column in zip(prices.dtypes, prices.columns):
    data_types[column] = str(data_type)

print(data_types)

columns = prices.columns

actions = []
index = 1
for i, price_row in prices.iterrows():
    price = {}
    for column in columns:
        # print(type(price_row[column]))
        # print(isinstance(price_row[column], int))
        if str(price_row[column]) == "nan":
            if data_types[column] == "object":
                price_row[column] = "UK"
            elif data_types[column] == "int64":
                price_row[column] = 0
            elif data_types[column] == "float64":
                price_row[column] = 0.0
        price[column] = price_row[column]
    action = {"index": {"_index": "house_prices", "_id": index}, "_op_type": "upsert"}
    doc = price
    actions.append(action)
    actions.append(json.dumps(doc))
    index += 1

res = es.bulk(index="house_prices", operations=actions)
print(res)
