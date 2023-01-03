from elasticsearch.exceptions import RequestError


def es_create_index_if_not_exists(elastic_instance, created_index):
    """Create the given ElasticSearch index and ignore error if it already exists"""
    try:
        elastic_instance.indices.create(index=created_index)
    except RequestError as ex:
        if ex.error == 'resource_already_exists_exception':
            print(f"The index {created_index} already exists")
        else: # Other exception - raise it
            print("Another error has occurred")