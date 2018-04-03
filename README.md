# Google Spreadhsheet Api - Values Batch Update

A [Supercode](http://gosupercode.com) function that update values multiple request in one call google spreadsheet.
Still developing for other methods of google spreadsheet api.

## Server Usage

[Supercode](http://gosupercode.com) SDK will be available after the launch.

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
        "valueInputOption": "USER_ENTERED",
        "data": [
            {
                "majorDimension": "ROWS",
                "range": "Sheet1!A1:A1",
                "values": [["Hello"]]
            },
            {
                "majorDimension": "ROWS",
                "range": "Sheet1!A2:A2",
                "values": [["World"]]
            }
        ]
    }'
    
    python test.py --credentials_json_data=$json_data --spreadsheet_id="<your spreadsheet id>" --payload=$payload


**Note:** Supercode has not been launched yet. This is for internal testing only.
