curl -X PUT "localhost:9200/documents" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "data": {
        "type": "text"
      },
      "attachment": {
        "properties": {
          "content": {
            "type": "text"
          },
          "title": {
            "type": "text"
          },
          "author": {
            "type": "text"
          },
          "content_type": {
            "type": "text"
          },
          "content_length": {
            "type": "integer"
          },
          "language": {
            "type": "text"
          },
          "date": {
            "type": "date",
            "format": "strict_date_optional_time||epoch_millis"
          },
          "keywords": {
            "type": "text"
          }
        }
      }
    }
  }
}
'