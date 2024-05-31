import fitz  # PyMuPDF
from elasticsearch import Elasticsearch

# Connect to the local Elasticsearch instance
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Define the index name
index_name = 'documents'

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

# Function to index text into Elasticsearch
# probably need this here instead: https://stackoverflow.com/questions/37861279/how-to-index-a-pdf-file-in-elasticsearch-5-0-0-with-ingest-attachment-plugin?rq=1, https://stackoverflow.com/questions/34857179/how-to-index-a-pdf-file-in-elasticsearch
def index_pdf_to_elasticsearch(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    document = {
        'content': text
    }
    es.index(index=index_name, document=document)


def search_elasticsearch(query):
    response = es.search(
        index=index_name,
        body={
            "query": {
                "match": {
                    "content": query
                }
            }
        }
    )
    return response

if __name__ == "__main__":
    pdf_path = 'path/to/your/document.pdf'
    index_pdf_to_elasticsearch(pdf_path)
    print("PDF content indexed successfully.")

    

if __name__ == "__main__":
    query = input("Enter your search query: ")
    response = search_elasticsearch(query)
    for hit in response['hits']['hits']:
        print(f"Document ID: {hit['_id']}\nContent: {hit['_source']['content']}\n") # need the source and content stuff here later when using the ai to also output the source file