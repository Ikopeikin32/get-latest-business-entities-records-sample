<p align="center">
    <img alt="alt_text" width="40px" src="favicon.ico" />  eDataPOle - Business Connect  https://edatapole.com/
</p>

# Sample code to fetch new registrated business entities information using REST API call.

To run a sample
1. Get access token - [sign-up](https://edatapole.com/profile) in www.eDataPole.com. Subscription is free and does not requred credit card information
2. download get-business-sample.py sample code and place your token access. 

```python
    # replace with your API CODE.
    # You can find access code on 
    # https://www.eDataPole.com/profile paqe.
    # or you can use a temporary demo api key is expiring on 9/15/2024 
    # api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjExMzc2MDcsImV4cCI6MTcyNjMyMTYwNywic3ViIjoiREVNTyJ9._ckRMgdDQL0wMjDwNmS4yHmwuoRd8U9uu7T7NDGg-Ow"
```

3. run
   python get-business-sample.py
 
Sample code below shows REST API  request parameters usage and handling the response.

```python
    # replace with your access code.
    #You can find access code on https://www.eDataPole.com/profile paqe.
    access_token="eyJhbG-Uxl0WHp98Q"
    host="edatapole.com"
    port = 80
    # GET request parameters
    # State. Currently only ny and fl are available
    state="NY"
    # Fetch entities filed since this date
    after_date="2024-06-20"
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

```
Same call with curl:
```curl
curl -v "http://edatapole.com/api/messages/bsns?st=NY&after=2024-06-15&new=1&api_key=YOUR_API_KEY"
```

Below is the response sample:

```python
{
  "list": [
    {
      "corp_name": "HIRE ORBITT LLC",
      "county": "Westchester",
      "dos_id": "7338074",
      "eff_date": "2024-07-27",
      "entity_type": "DOMESTIC LIMITED LIABILITY COMPANY",
      "for_juris": "NY",
      "id": 3922,
      "sop_addr1": "95 Circle Drive",
      "sop_addr2": "",
      "sop_city": "Hastings on Hudson",
      "sop_name": "Hire Orbitt LLC",
      "sop_state": "NY",
      "sop_zip": "10706"
    },
    {
      "corp_name": "LYLA SPA INC.",
      "county": "New York",
      "dos_id": "7339633",
      "eff_date": "2024-08-01",
      "entity_type": "DOMESTIC BUSINESS CORPORATION",
      "for_juris": "NY",
      "id": 7218,
      "sop_addr1": "31 DIVISION STREET",
      "sop_addr2": "BASEMENT",
      "sop_city": "NEW YORK",
      "sop_name": "RONG WU",
      "sop_state": "NY",
      "sop_zip": "10002"
    }
  ],
  "response_status": 200,
  "response_reason": "OK"
}
```
