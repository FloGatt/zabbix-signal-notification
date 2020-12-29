#!/bin/bash

to=$1
message=$2

post_payload()
{
  cat <<EOF
{
  "message": "$message",
  "number":"<sender>" ,
  "recipients": ["$to"]
}
EOF
}

curl -X POST -H "Content-Type: application/json" -d "$(post_payload)" 'http://127.0.0.1:8080/v2/send'
