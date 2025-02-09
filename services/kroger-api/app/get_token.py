from datetime import datetime, timedelta
import base64
import json
import requests

def get_token(scope):
    try:
        # Open Variables file and set client_id and client_secret variables
        with open("Credentials.json", "r") as file:
            variables = json.load(file)
            client_id = variables["client_id"] 
            client_secret = variables["client_secret"] 
            oldtoken = variables["token"]
            expiration = datetime.strptime(variables['expiration'], '%Y-%m-%d %H:%M:%S')
            current_dt = datetime.now().replace(microsecond=0) 
        
        if expiration > current_dt:
            print("Using Old Token")
            return oldtoken
        else:
            print("Fetching New Token")

            # Create the base64 encoded credentials
            credentials = f'{client_id}:{client_secret}'
            encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

            # Define the URL, headers, and request data
            token_url = 'https://api.kroger.com/v1/connect/oauth2/token'
            headers = {
                'Accept': 'application/json',  # You might prefer JSON for easier handling
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': f'Basic {encoded_credentials}'
            }
            data = f'grant_type=client_credentials&scope={scope}'

            # Make the POST request
            response = requests.post(token_url, headers=headers, data=data)
            
            # Check if the request was successful
            if response.status_code == 200:
                response_data = response.json()
                token = response_data['access_token']
                expiration_seconds = response_data['expires_in']
                new_expiration = current_dt + timedelta(seconds=expiration_seconds)
                
                # Save the new token and expiration in Credentials.json
                data = {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "token": token,
                    "expiration": str(new_expiration)
                }
                with open("Credentials.json", "w") as file:
                    json.dump(data, file)
                
                print("Using New Token")
                return f"Bearer {token}"
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None
    except Exception as e:
        print(f"We have an exception: {str(e)}")
        return None
    
get_token("product.compact")
