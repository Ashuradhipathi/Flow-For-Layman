import streamlit as st
import pandas as pd
import re  # For URL validation
from IPython.display import HTML  # For iframe embedding

# Placeholder data for demonstration
data = {
    'ID': [1, 2, 3],
    'Name': ['Website 1', 'Website 2', 'Website 3'],
    'URL': ['https://www.google.com/', 'https://www.im45145v.dev/', 'invalid_url']
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
st.set_page_config(page_title="Interactive Dashboard with Grid and Iframes")

st.title("My Dashboard")

# Define an empty container below the grid for the iframe
preview_container = st.empty()

# Iterate through the dataframe and create grids with buttons
for i, row in df.iterrows():
    grid = st.columns([1, 1, 3, 2])  # Create a 4-column grid for each row

    with grid[0]:
        st.write(row['ID'])  # Display ID in first column

    with grid[1]:
        st.write(row['Name'])  # Display name in second column

    with grid[2]:
        link_text = f"[**{row['Name']}**]({row['URL']})"  # Combine name and link
        st.markdown(link_text, unsafe_allow_html=True)  # Display link with formatting

    with grid[3]:
        if st.button('Preview', key=f'edit_button{i}'):
            # Handle button click (replace with your desired functionality)
            if row['URL'] == 'invalid_url':
                st.error("Invalid URL entered")
            else:
                # Move to the preview container below the grid
                with preview_container:
                    # Clear the container before embedding iframe
                    preview_container.empty()
                    st.write(embed_iframe(row['URL']))  # Embed iframe on button click

