import streamlit as st


image , document = st.tabs(["Images","Documents"])

with image:
    uploaded_image = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)

with document:
    uploaded_document = st.file_uploader("Upload Document", type=["pdf","txt"])

    if uploaded_document is not None:
        st.write(uploaded_document.read())
