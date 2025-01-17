"""Module providing a function making  call eDataPole REST API."""

import http.client
import sys
import json
import urllib.parse

RSP_STATUS = "response_status"
RSP_REASON = "response_reason"


def fetch_entities(host, port, access_token, state, after_date, new_or_closed=1):
    """This is a function to fetch  new open corporations"""
    try:

        conn = http.client.HTTPConnection(host, port)
        # Connect to host
        conn.connect()

        query = {
            "st": state,
            "after": after_date,
            "new": new_or_closed,
            "api_key": access_token,
        }
        params = "/api/messages/bsns?" + urllib.parse.urlencode(query)

        print(params)
        # This will send a request to the server using the HTTP request
        # GET method /api/messages/bsns?st=...& after=...&new=...&apy_key=...
        conn.request("GET", params)
        response = conn.getresponse()
        data = response.read()
        entity_list = json.loads(data)
        entity_list[RSP_STATUS] = response.status
        entity_list[RSP_REASON] = response.reason
        return entity_list
    except Exception as e:
        print(e)
        error = {
            RSP_STATUS: 999,
            RSP_REASON: e,
        }
        return error
    finally:
        # Close the connection to the server.
        conn.close()


if __name__ == "__main__":
    # replace with your access code.
    # You can find access code on https://www.eDataPole.com/profile paqe.
    # this is a demo key with expiration on 9/15/24
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjExMzc2MDcsImV4cCI6MTcyNjMyMTYwNywic3ViIjoiREVNTyJ9._ckRMgdDQL0wMjDwNmS4yHmwuoRd8U9uu7T7NDGg-Ow"
    host = "edatapole.com"
    port = 80
    #host = "127.0.0.1"
    #port = 6060
    # GET request parameters
    # State. Currently only NY and FL are available
    state = "NY"
    # Fetch entities filed since this date
    after_date = "2024-07-15"
    # Specify new and closed entities. 1 fro new, and 0 for closed
    new_or_closed = 1
    json_response = fetch_entities(
        host, port, api_key, state, after_date, new_or_closed
    )
    print(json_response)
    if json_response[RSP_STATUS] != 200:
        print("Exception fetching data")
        print(json_response[RSP_STATUS], json_response[RSP_REASON])
        sys.exit()
    # if request is successful
    if "list" in json_response:
        entities = json_response["list"]
        print("-----------------Returned entities-------------")
        for entity in entities:
            print(entity["id"], entity)
