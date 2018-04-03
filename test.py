from googleapiclient import discovery
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
import httplib2, socket


SHEETS_DISCOVERY_URL='https://sheets.googleapis.com/$discovery/rest?version=v4'
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'


class GoogleSpreadsheet:
    def __init__(self, credentials_json_data, spreadsheet_id, payload=None):
        self.credentials_json_data = credentials_json_data
        self.spreadsheet_id = spreadsheet_id
        self.payload = payload

    def get_sheets_service(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(self.credentials_json_data, scopes=SCOPES)
        http = credentials.authorize(httplib2.Http(timeout=120))

        return discovery.build(
            'sheets',
            'v4',
            http=http,
            discoveryServiceUrl=SHEETS_DISCOVERY_URL
        )

    def values_batch_update(self):
        service = self.get_sheets_service()

        try:
            result = service.spreadsheets().values().batchUpdate(
                spreadsheetId=self.spreadsheet_id, body=self.payload).execute()

            response = {
                "data": result
            }

        except (httplib2.HttpLib2Error, socket.error) as ex:
            response = {
                "error": {
                    "code": 408,
                    "message": "Timeout error. Acessing google spreadsheet api."
                }
            }

        except (HttpError) as ex:
            response = {
                "error": {
                    "code": 400,
                    "message": ex
                }
            }

        return response


def main(credentials_json_data=None, spreadsheet_id="", payload=None):
    google_spreadsheet = GoogleSpreadsheet(
        credentials_json_data=credentials_json_data,
        spreadsheet_id=spreadsheet_id,
        payload=payload,
    )

    response = google_spreadsheet.values_batch_update()

    print response
    return response


if __name__ == '__main__':
    import argparse
    import json
    import ast

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--spreadsheet_id',
        help="Id of the spreadsheet."
    )
    parser.add_argument(
        '--credentials_json_data',
        help="Crendential from google appengine service account. Pass it as json converted as string"
    )
    parser.add_argument(
        '--payload',
        help="Payload data"
    )

    args = parser.parse_args()
    args.payload = json.loads(args.payload)
    print args.payload
    args.credentials_json_data = json.loads(args.credentials_json_data)

    main(**vars(args))
