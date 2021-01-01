#!/usr/bin/python3

import sys
import requests

if len(sys.argv) != 4:
    sys.exit(0)

SIGNAL_GATEWAY_URL = "http://localhost:8080/v2/send"
FROM = "+49123456789"

# (sys.argv[1] == {ALERT.SENDTO}, sys.argv[2] == {ALERT.SUBJECT}, sys.argv[3] == {ALERT.MESSAGE})
PAYLOAD = {
    "message": str(sys.argv[2]) + "\n\n" + str(sys.argv[3]),
    "number": FROM,
    "recipients": [str(sys.argv[1])]
}

try:
    response = requests.post(SIGNAL_GATEWAY_URL, json=PAYLOAD)
except:
    print("An error has occured:", sys.exc_info()[0])

