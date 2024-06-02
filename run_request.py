import os
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.core.credentials import AzureKeyCredential
from elasticsearch import Elasticsearch

# Azure Cognitive Services credentials
azure_endpoint = "https://dsproject.cognitiveservices.azure.com/"
azure_api_key = "1041c8be86c14b9ebe6dcfe758c875f9"

project_name = "DataScienceProject"
deployment_name = "test"

# Elasticsearch setup
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Initialize the Azure Question Answering client
qa_client = QuestionAnsweringClient(azure_endpoint, AzureKeyCredential(azure_api_key))

def search_elasticsearch(query):
    # Query Elasticsearch
    response = es.search(
        index="my-index-000001",
        body={
            "query": {
                "match": {
                    "content": query
                }
            }
        }
    )
    return response

def get_best_answer(question):
    # Search Elasticsearch for relevant documents
    es_response = search_elasticsearch(question)
    
    # Extract the relevant text from the Elasticsearch response
    passages = [hit['_source']['content'] for hit in es_response['hits']['hits']]
    context = " ".join(passages)

    # Use Azure Question Answering to get the best answer
    answer = qa_client.get_answers_from_text(
            question=question,
            text_documents=[context]
        )

    for candidate in answer.answers:
        print("({}) {}".format(candidate.confidence, candidate.answer))
        print("Source: {}".format(candidate.source))

if __name__ == "__main__":
    question = input("Ask a question: ")
    answer = get_best_answer(question)
    print(f"Answer: {answer}")