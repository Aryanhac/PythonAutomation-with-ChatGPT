import requests

api_url = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer "+api_key
}

request_body ={
    "model": "text-davinci-003",
    "prompt": "Write the python script for writing hello world",
    "max_tokens": 100,
    "temperature": 0
}


response = requests.post(api_url,headers=request_headers,json=request_body)
 

if response.status_code == 200:
   print(f"response: {response.json()}")
else:
   print(f"Some error occured: {response.status_code}")   
