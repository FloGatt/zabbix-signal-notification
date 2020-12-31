#!/bin/bash

to=$1
subject=$2
message=$3

post_payload()
{
  cat <<EOF
{
  "message": "$subject: $message",
  "number":"<sender>",
  "recipients": ["$to"]
}
EOF
}

curl -X POST -H "Content-Type: application/json" -d "$(post_payload)" 'http://127.0.0.1:8080/v2/send'
