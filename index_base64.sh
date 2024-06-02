curl -X PUT "localhost:9200/my-index-000001/_doc/my_id?pipeline=attachment&pretty" -H 'Content-Type: application/json' -d'
{
  "data": "'"output.txt"'"
}
'

