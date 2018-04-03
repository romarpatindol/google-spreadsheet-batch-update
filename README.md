# Google Spreadhsheet Api - Batch Update

A [Supercode](http://gosupercode.com) function that applies one or more updates to the spreadsheet.

## Server Usage
#Get the Supercode Python SDK: https://git.io/vxTjp
```
import supercode
import pprint

credentials_json_data = {}
payload={}

response = supercode.call(
    "super-code-function",
    "your-supercode-api-key",
    credentials_json_data,
    spreadsheet_id,
    payload
)

pprint(response)
```

## Testing on Command Line
`python test.py --help`

example: 

    json_data='{
      "type": "service_account",
      "project_id": "symph-git-hooks",
      "private_key_id": "",
      "private_key": "",
      "client_email": "",
      "client_id": "",
      "auth_uri": "",
      "token_uri": "",
      "auth_provider_x509_cert_url": "",
      "client_x509_cert_url": ""
    }'
    
    payload='{
        requests: [
            {
                "insertDimension": {
                    "range": {
                        "sheetId": 5125512, #the sheet ID
                        "dimension": "COLUMNS",
                        "startIndex": 2,
                        "endIndex": 3
                    }
                }
            }
        ]
    }'
    
    python test.py --credentials_json_data=$json_data --spreadsheet_id="<your spreadsheet id>" --payload=$payload
