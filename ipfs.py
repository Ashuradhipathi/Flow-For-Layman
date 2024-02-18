from pinatapy import PinataPy
import requests
import os
def ipfs_upload(uploaded_file):
    gateway="https://ipfs.io/ipfs/"
    path = None
    if uploaded_file:
            path = ("temp"+uploaded_file.name)
            with open(path, "wb") as f:
                    f.write(uploaded_file.getvalue())
    if path:
        pinata = PinataPy("", "")
        print("path", path.replace(os.sep, '/'))
        result = pinata.pin_file_to_ipfs(path.replace(os.sep, '/'))
        print("File uploaded to IPFS succesfully!")
        print(result)
        os.remove(path)
        return (result['IpfsHash'], gateway+result['IpfsHash'])
        