import requests
import json 

projectId = ""
projectSecret = ""
endpoint = "https://ipfs.infura.io:5001"

### CREATE AN ARRAY OF TEST FILES ###
files = {
    'file': 'myNFT.png'
}

### ADD FILE TO IPFS AND SAVE THE HASH ###
response1 = requests.post(endpoint + '/api/v0/add', files=files, auth=(projectId, projectSecret))
print(response1)
hash = response1.text.split(",")[1].split(":")[1].replace('"','')
print(hash)

params = {
    'arg': hash
}
response2 = requests.post(endpoint + '/api/v0/cat', params=params, auth=(projectId, projectSecret))
print(response2)
print(response2.text)
