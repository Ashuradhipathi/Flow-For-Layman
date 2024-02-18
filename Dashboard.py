import streamlit as st
import flow_functions
import asyncio
from IPython.display import HTML  # For iframe embedding
from streamlit_extras.switch_page_button import switch_page

# Testnet account name
acc_name = "web3hacks"

# Testnet account address
acc_address = "0x429b022e4a4860c5"

# Flow config path
config_path = "./flow/flow.json"


if "currentdata" not in st.session_state:
    st.session_state["currentdata"]={}
if "fetch" not in st.session_state:
    st.session_state["fetch"]=False
if "nft_data" not in st.session_state:
    st.session_state["nft_data"]={}
if "ids" not in st.session_state:
    st.session_state["ids"]=[]
def embed_iframe(url):
    iframe_html = f"""
    <iframe src="{url}" style="width: 100%; height: 300px;"></iframe>
    """
    return HTML(iframe_html)

preview_container = st.empty()


st.title("My IP NFTs")

st.subheader("All intellectual property minted as NFTs displayed here. Click on the preview button to view the NFT.")
st.write("\n\n")
st.write("\n\n")
st.markdown(f"##### Account address: :green[{acc_address}]")
st.write("\n\n")
st.write("\n\n")
if not st.session_state["fetch"]:
    x = flow_functions.all_nfts()
    RetrieveNFTClass = flow_functions.RetrieveAllNFTs(acc_address)
    ids = asyncio.run(RetrieveNFTClass.run(ctx = flow_functions.Config(config_path, acc_name)))
# Create a list of dictionaries, ensuring consistent keys for grid display
    nft_data = [
        nft for nft in x.values()
    ]
    st.session_state["fetch"]=True 
    st.session_state["ids"]=ids
    print(st.session_state["ids"])
    st.session_state["nft_data"]=nft_data
else:
    RetrieveNFTClass = flow_functions.RetrieveAllNFTs(acc_address)
    ids = asyncio.run(RetrieveNFTClass.run(ctx = flow_functions.Config(config_path, acc_name)))
    new_ids = [id for id in ids if id not in st.session_state["ids"]]

    nft_data = st.session_state["nft_data"]
    print(new_ids)
    for id in new_ids:
        print(id)
        nft_data.append(flow_functions.nft_data(acc_address, acc_name, id))
    
grid = st.columns([1, 1.5, 2])  # Create a 3-column grid for each NFT
with grid[0]:
    st.subheader("Name:")
with grid[1]:
    st.subheader("IPFS:")
with grid[2]:
    st.subheader("Preview:")
st.divider()
i=0
new_data = []
b= set()
for nft in nft_data:
    if "ipfsHash" in nft and nft["ipfsHash"] not in b:
        new_data.append(nft)
        b.add(nft["ipfsHash"])

for nft in new_data:
    grid = st.columns([1, 1.5, 2])  # Create a 3-column grid for each NFT        
    with grid[0]:
        st.write(nft.get("name","N/A"))
    with grid[1]:
        st.write(nft.get("ipfsHash","N/A"))
        lin=nft.get("ipfsHash","N/A")
    with grid[2]:
        if st.button('Preview', key=f'edit_button{i}'):
            st.session_state["currentdata"]=nft
            switch_page("view")
    i+=1
    st.divider()