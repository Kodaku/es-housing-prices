import json


def add_data(es, prices, data_types):
    actions = []
    index = 1
    for i, price_row in prices.iterrows():
        price = {}
        for column in prices.columns:
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
