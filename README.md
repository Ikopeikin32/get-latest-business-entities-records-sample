<p align="center">
    <img src="https://edatapole.com/static/media/logo.7f2f080730cf78b567f0.png" width="20%" alt="eDataPole logo" />
</p>

# Sample code to fetchnew registrated business entities information using REST API call.

To run a sample
1. Get access token - [sign-up](https://edatapole.com/profile)  www.eDataPole.com. Subscription is free and does not requred credit card information
2. download get-business-sample.py sample code and place your token access. 

```python
    # replace with your access code.
    # You can find access code on 
    # https://www.eDataPole.com/profile paqe.
    access_token="eyJhbG...ciOiJS98Q"
```

3. run
   python get-business-sample.py
 
Sample code below shows the GET request parameters usage

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