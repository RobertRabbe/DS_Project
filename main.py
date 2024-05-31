import os
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.core.credentials import AzureKeyCredential
from elasticsearch import Elasticsearch

# Azure Cognitive Services credentials
azure_endpoint = "https://<your-endpoint>.cognitiveservices.azure.com/"
azure_api_key = "<your-api-key>"

# Elasticsearch setup
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Initialize the Azure Question Answering client
qa_client = QuestionAnsweringClient(azure_endpoint, AzureKeyCredential(azure_api_key))

def search_elasticsearch(query):
    # Query Elasticsearch
    response = es.search(
        index="your_index",
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
    answer = qa_client.get_answers(
        question=question,
        documents=[context]
    )

    if answer.answers:
        return answer.answers[0].answer
    else:
        return "I'm sorry, I couldn't find an answer to your question."

if __name__ == "__main__":
    question = input("Ask a question: ")
    answer = get_best_answer(question)
    print(f"Answer: {answer}")