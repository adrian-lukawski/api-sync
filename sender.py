import gzip
import json
import requests
import time
from StringIO import StringIO

STATUS_CODE = 202
API_VERSION = 10
API_KEY = 'putApiKeyHere' # api key
URL = 'http://api.kontakt.io/event/collect'
GATEWAY_UNIQUE_ID = 'putApUniqueIdHere' # AP unique id

headers = {
	'Api-Key': API_KEY,
	'Accept': 'application/vnd.com.kontakt+json; version={}'.format(API_VERSION),
	'Content-Type': 'application/json',
	'Content-Encoding': 'gzip', # inform that payload is compressed in GZIP
	'Connection': 'keep-alive' # reuse single connection for many request-response exchanges
}

timestamp = int(time.time())

payload = {
  "events": [{
      "rssi": -50,
      "data": "AgEGGv9MAAIVg4f8zZ21QWOGGOhYcVXUTv//AAD0",
      "srData": "ChYN0HlhdW00MjI=",
      "timestamp": timestamp,
      "scanType": "BLE",
      "deviceAddress": "f9:10:e1:40:d4:f1"
    }
  ],
  "version": 3,
  "proto": "DEFAULT",
  "sourceId": GATEWAY_UNIQUE_ID,
  "timestamp": timestamp
}

compressed_body = StringIO()
gz = gzip.GzipFile(fileobj=compressed_body, mode="wb") # GZIP payload
gz.write(json.dumps(payload))
gz.close()

response = requests.post(URL, data=compressed_body.getvalue(), headers=headers)

if response.status_code == STATUS_CODE: print 'Success'
else: print 'something went wrong (http status code: {})'.format(response.status_code)
