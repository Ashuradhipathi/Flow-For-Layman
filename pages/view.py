import streamlit as st
from IPython.display import HTML  # For iframe embedding
def embed_iframe(url):
    # if not re.match(r"https?://(?:[a-zA-Z0-9-\.]+\.)+[a-zA-Z]{2,6}(?:/[^\s]*)?", url):
    #     return f"Invalid URL: {url}"

    iframe_html = f"""
    <iframe src="{url}" style="width: 100%; height: 300px;"></iframe>
    """
    return HTML(iframe_html)
try:
    nft = st.session_state["currentdata"]
    preview_container = st.empty()
    lin = nft.get("ipfsHash", "N/A")

    with preview_container:
        preview_container.empty()
        st.write(embed_iframe(f"https://ipfs.io/ipfs/{lin}"))
    st.write(nft)      
except Exception as e:
    st.write("Nothing is here")
