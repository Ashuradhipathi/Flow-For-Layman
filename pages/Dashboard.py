import streamlit as st
import pandas as pd
import re  # For URL validation
from IPython.display import HTML  # For iframe embedding

# Placeholder data for demonstration
data = {
    'ID': [1, 2, 3],
    'Name': ['Website 1', 'Website 2', 'Website 3'],
    'URL': ['https://www.example.com/1', 'https://www.example.com/2', 'invalid_url']
}
df = pd.DataFrame(data)

# Function to validate URLs and embed iframes
def embed_iframe(url):
    if not re.match(r"https?://(?:[a-zA-Z0-9-\.]+\.)+[a-zA-Z]{2,6}(?:/[^\s]*)?", url):
        return f"Invalid URL: {url}"

    iframe_html = f"""
    <iframe src="{url}" style="width: 100%; height: 300px;"></iframe>
    """
    return HTML(iframe_html)

# Create the Streamlit app
st.set_page_config(page_title="Interactive Dashboard with Table and Iframes")

st.title("My Dashboard")

# Display the table and buttons in separate columns
col1, col2 = st.columns(2)
col1.header("My NFT")

col1.table(df[['Name']])  # Display only name in the first column
col2.header('Preview')  # Clear header for the second column

# Create a container to consistently place iframes below everything
preview_container = st.empty()

# Add interactivity and iframe embedding
for i, row in df.iterrows():
    url = row['URL']
    name = row['Name']

    # Create button and handle click event
    with col2:
        if st.button(name):
            if url == 'invalid_url':
                st.error("Invalid URL entered")
            else:
                # Clear the preview container before embedding iframe
                preview_container.empty()
                # Embed iframe in the dedicated container with full width
                with preview_container:
                    st.write(embed_iframe(url))

