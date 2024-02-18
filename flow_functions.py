from mint import *
from ipfs import ipfs_upload

# Testnet account name
acc_name = "web3hacks"

# Testnet account address
acc_address = "0x429b022e4a4860c5"

# Flow config path
config_path = "./flow/flow.json"

def mint_file(uploaded_file, description, type, acc_address, receiver_address,  acc_name):
    ipfs_hash, ipfs_link = ipfs_upload(uploaded_file)
    
    data = {
        "name": uploaded_file.name,
        "ipfsLink": ipfs_link,
        "ipfsHash": ipfs_hash,
        "description": description,
        "type": type
    }
    
    MintClass = MintNFT(acc_address, receiver_address, data)
    
    # Replace with streamlit spinner?
    print("Minting NFT...")
    
    asyncio.run(MintClass.run(ctx = Config(config_path, acc_name)))
    print("NFT minted successfully!")

def nft_data(acc_address, acc_name, id):
    MetaDataClass = RetrieveMetadata(acc_address, id)
    data = asyncio.run(MetaDataClass.run(ctx = Config(config_path, acc_name)))
    return data

def all_nfts(acc_address, acc_name):
    RetrieveNFTClass = RetrieveAllNFTs(acc_address)
    ids = asyncio.run(RetrieveNFTClass.run(ctx = Config(config_path, acc_name)))
    all_data = {}
    for id in ids:
        all_data[id] = nft_data(acc_address, acc_name, id)
    return all_data