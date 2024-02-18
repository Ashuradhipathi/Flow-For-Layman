import streamlit as st
from IPython.display import HTML  # For iframe embedding
def embed_iframe(url):
    # if not re.match(r"https?://(?:[a-zA-Z0-9-\.]+\.)+[a-zA-Z]{2,6}(?:/[^\s]*)?", url):
    #     return f"Invalid URL: {url}"

    iframe_html = f"""
    <iframe src="{url}" style="width: 100%; height: 800px;"></iframe>
    """
    return HTML(iframe_html)
try:
    nft = st.session_state["currentdata"]
    
    lin = nft.get("ipfsHash", "N/A")
    st.title("NFT Viewer")
    
    st.markdown(f"## Name: :blue[ {nft.get('name', 'N/A')} ]")
    st.subheader("Preview")
    preview_container = st.empty()
    with preview_container:
        preview_container.empty()
        st.write(embed_iframe(f"https://ipfs.io/ipfs/{lin}"))
    st.write("\n\n")
    st.header("Details")
    st.divider()
    st.markdown(f"### IPFS Hash: ") 
    st.markdown(f"### :green[ {lin} ]")
    link = f"https://ipfs.io/ipfs/{lin}"
    st.markdown(f"Visit your file stored in IPFS: [Link to IPFS]({link})")
    st.divider()
    st.markdown(f"### Type: ")    
    st.markdown(f"### :green[ {nft.get('type', 'N/A')} ]")
    st.divider()
    st.markdown(f"### Description: ")
    st.markdown(f"### :green[ {nft.get('description', 'N/A')} ]")
    
except Exception as e:
    st.write("Nothing is here")
