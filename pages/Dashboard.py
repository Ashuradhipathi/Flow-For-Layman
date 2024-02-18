import streamlit as st
from flow_functions import *
from IPython.display import HTML  # For iframe embedding
from streamlit_extras.switch_page_button import switch_page
if "currentdata" not in st.session_state:
    st.session_state["currentdata"]={}
def embed_iframe(url):
    iframe_html = f"""
    <iframe src="{url}" style="width: 100%; height: 300px;"></iframe>
    """
    return HTML(iframe_html)
x = all_nfts()
preview_container = st.empty()


# Create a list of dictionaries, ensuring consistent keys for grid display
nft_data = [
    nft for nft in x.values()
]
grid = st.columns([1, 2, 2])  # Create a 3-column grid for each NFT
with grid[0]:
    st.write("Name:")
with grid[1]:
    st.write("IPFS:")
with grid[2]:
    st.write("Preview:")
i=0
for nft in nft_data:
    i+=1
    with grid[0]:
        st.write(nft.get("name","N/A"))
    with grid[1]:
        st.write(nft.get("ipfsHash","N/A"))
        lin=nft.get("ipfsHash","N/A")
    with grid[2]:
        if st.button('Preview', key=f'edit_button{i}'):
            st.session_state["currentdata"]=nft
            switch_page("view")