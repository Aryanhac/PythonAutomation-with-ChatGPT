import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="prompt that pass to openAI")
parser.add_argument("filename", help="name of new file")
args = parser.parse_args()


api_url = "https://api.openai.com/v1/completions"

api_key = os.getenv("OPENAI")

request_headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer "+api_key
}

request_body ={
    "model": "text-davinci-003",
    "prompt": f"Write the python script for {args.prompt}. Only Code not text",
    "max_tokens": 500,
    "temperature": 0.5
}


response = requests.post(api_url,headers=request_headers,json=request_body)
 

if response.status_code == 200:
   text = response.json()['choices'][0]['text']
   with open(args.filename,'w') as file:
       file.write(text)
else:
   print(f"Some error occured: {response.json()}")   
