from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

def search_elasticsearch(query):
    response = es.search(
        index="documents",
        body={
            "query": {
                "match": {
                    "attachment.content": query
                }
            }
        }
    )
    return response

if __name__ == "__main__":
    query = input("Enter your search query: ")
    response = search_elasticsearch(query)
    for hit in response['hits']['hits']:
        print(f"Document ID: {hit['_id']}")
        print(f"Title: {hit['_source']['attachment']['title']}")
        print(f"Author: {hit['_source']['attachment']['author']}")
        print(f"Content: {hit['_source']['attachment']['content']}\n")