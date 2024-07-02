"""Module providing a function making http call."""
import http.client
import sys
import json
import urllib.parse

RESPONSE_STATUS="response_status"
RESPONSE_REASON="response_reason"

def fetch_entities(host,port,access_token, state, after_date,new_or_closed=1):
    """This is a function to fetch  new open corporations"""
    try:
        
        conn = http.client.HTTPConnection(host,port)
        # pass access token with header
        headers = { 'authorization': "Bearer "+ access_token}
        #Connect to the host
        conn.connect()
        query = {
            'st': state,
            'after': after_date,
            'new': new_or_closed,
        }
        params = "/api/messages/bsns?" + urllib.parse.urlencode(query)
        
        print(params)
        #This will send a request to the server using the HTTP request GET method /api/messages/bsns?st=...& after=...&new=...
        conn.request("GET", params, headers=headers)
        response = conn.getresponse()
        data = response.read()
        #Close the connection to the server.
    except Exception as e:
        print(e)
        error = {
            RESPONSE_STATUS: 999,
            RESPONSE_REASON: e,
        }
        return error
    finally:
        conn.close()
    entity_list=json.loads(data)
    entity_list[RESPONSE_STATUS] = response.status
    entity_list[RESPONSE_REASON] = response.reason
    return entity_list

if __name__ == "__main__":
    host="edatapole.com"
    port = 80
    access_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJQczFEUnVNUnFsX29WWTRDZGJuYSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jMjJwaGRqbTZzMnI1NGpoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjdhYTAxNDViN2IyZWRmN2Y4NzZlNDgiLCJhdWQiOlsiaHR0cHM6L2VEYXRhUG9sZVNlcnZlci5jb20iLCJodHRwczovL2Rldi1jMjJwaGRqbTZzMnI1NGpoLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTk5MjQ4NDQsImV4cCI6MTcyMDAxMTI0NCwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6ImJMRU53R29qR2NTbzhwRjNJNjQ0STFhTjlzWHZ5eG83IiwicGVybWlzc2lvbnMiOltdfQ.M9Yk_SovtnxrWefHwhbBDWri_zOIKnDTl-8UE4E3csl6ByTQzVgFeEYQOW2YwHykxFLUc1hfYoWFHrXvuS9TKCTj7xrMM9OXIkWW1OIt81_HdFYI-m8GZxR510vYpj6p7wbmxeQVnWaG0F-Ghq-_93rdsU0JXX8KgUf2UG3yzKGVdXrybKALGrWNbldO40iyc44ufZMgL0g6xvwIUVQgClGuXhlcr0INDWcsrpQFvnN6pZbiGbDk9YYxdcMed_lBoVQ7U8tBF7r1Z-hRhi1_WdkgT4SQm8ExGgrv0JvTqf3EJcjWsOKG4ISmB0IkvhA4AuQT4NfPE5U-Uxl0WHp98Q"
    state="NY"
    after_date="2024-06-20"
    new_or_closed=1
    response = fetch_entities(host,port, access_token, state, after_date,new_or_closed)
    print(response) 
    if response[RESPONSE_STATUS] !=200:
        print("Exception fetching data")
        print(response[RESPONSE_STATUS],response[RESPONSE_REASON])
        sys.exit() 
    # if request is successful 
    if 'list' in response: 
        entities=response['list']
        print("-----------------Returned entities-------------")
        for entity in entities:
            print(entity['id'],entity)
        sys.exit() 


   