import streamlit as st
import base64
from flow_functions import mint_file

def displayPDF(uploaded_file):
    
    # Read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Convert to utf-8
    base64_pdf = base64.b64encode(bytes_data).decode('utf-8')

    # Embed PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="600" type="application/pdf"></iframe>'

    # Display file
    st.markdown(pdf_display, unsafe_allow_html=True)

image ,text,  pdf = st.tabs(["Images","Text Document","PDF"])

with image:
    uploaded_image = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
        mint_file(uploaded_image)
        with st.spinner("Minting NFT.."):
            transaction_id, ipfs_link =  mint_file(uploaded_image)
        st.markdown(f"Visit your file stored in IPFS: [{ipfs_link}]({ipfs_link})")
        st.markdown(f"*Transaction id*: {transaction_id}")
        st.markdown(f"*View Your Transaction on Flow Diver*: [{transaction_id}](https://testnet.flowdiver.io/tx/{transaction_id})")

with text:
    st.write("Upload a document")
    uploaded_document = st.file_uploader("Upload Document", type=["txt"])

    if uploaded_document is not None:
        st.write(uploaded_document.read())
        with st.spinner("Minting NFT.."):
            transaction_id, ipfs_link =  mint_file(uploaded_document)
        st.markdown(f"Visit your file stored in IPFS: [{ipfs_link}]({ipfs_link})")
        st.markdown(f"*Transaction id*: {transaction_id}")
        st.markdown(f"*View Your Transaction on Flow Diver*: [{transaction_id}](https://testnet.flowdiver.io/tx/{transaction_id})")
        






    
with pdf:
    
    st.write("Upload a pdf")
    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])


    if uploaded_pdf is not None:
        displayPDF(uploaded_pdf)
        with st.spinner("Minting NFT.."):
            transaction_id, ipfs_link =  mint_file(uploaded_document)
        st.markdown(f"Visit your file stored in IPFS: [{ipfs_link}]({ipfs_link})")
        st.markdown(f"*Transaction id*: {transaction_id}")
        st.markdown(f"*View Your Transaction on Flow Diver*: [{transaction_id}](h

