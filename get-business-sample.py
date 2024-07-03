"""Module providing a function making  call eDataPole REST API."""
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
        #This will send a request to the server using the HTTP request 
        #GET method /api/messages/bsns?st=...& after=...&new=...
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
    # replace with your access code.
    #You can find access code on https://www.eDataPole.com/profile paqe.
    access_token="eyJhbGciOiJSUzI1Rldi1jMjJwaGRqbTZzMnI1NGpoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjdhYTAxNDViN2IyZWRmN2Y4NzZlNDgiLCJhdWQiOlsiaHR0cHM6L2VEYXRhUG9sZVNlcnZlci5jb20iLCJodHRwczovL2Rldi1jMjJwaGRqbTZzMnI1NGpoLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTk5Mzk4OTgsImV4cCI6MTcyMjUzMTg5OCwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6ImJMRU53R29qR2NTbzhwRjNJNjQ0STFhTjlzWHZ5eG83IiwicGVybWlzc2lvbnMiOltdfQ.Ji4Pqr_gsBsd2fGSFQWyXuVol6KN5B_F8pxZhx9mXELukm9UDqyBjolMBP1bz3druaZ9gvxH-aXO3zHEsCAiNuRVU54_WvSbfLMvZ5mBeyuFOnRjC2i9DTgfjkIEGpDGvr7kw_D6eZdjZMZBDfmmzR0VYwhqzAyEVDrJPZ5frbgUV2zSQnaBdxiByJ0gykvVY2OpumHRgOkn23vZaoxeQ0nzh6In9bqg0folAG0QEX8y4RZpCNEtR1cfB6ow9zjBBn6zdJUc7zNAtx9AhWQjJCAFZK16nGZTVTqQKs2jkFLwt5O0qaTJ20_t5GEAKZJFjp6QZzG1MIUYmHAMobiD9A"
    host="edatapole.com"
    port = 80
#    host="127.0.0.1"
#    port = 6060
    # GET request parameters
    # State. Currently only ny and fl are available
    state="NY"
    # Fetch entities filed since this date
    after_date="2024-07-20"
    # Specify new and closed entities. 1 fro new, and 0 for closed
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


   