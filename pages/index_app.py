import google.generativeai 
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import os
import streamlit as st
from streamlit_ace import st_ace

GOOGLE_API_KEY = "AIzaSyA3dKe-L6S_3I1nXF3hwvJ-FO-MzfDPvtg"

#os.getenv("api_key")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


llm = Gemini(model="models/gemini-pro", temperature=0, embedding=GeminiEmbedding,)



def generate_legal_contracts(query):
    prompt = f"You are an experienced Cadence Smart Contract Engineer, with extensive experience of converting legal agreements into smart contracts to be used as Smart contracts. Using the legal agreement below, generate a Cadence smart contract that will represent the legal agreement on the blockchain, create functions in the cntract that represents the condirions of the legal agreement. You are only required to generate the code without any explanation, you may only add comments to the codex and use proper access specifiers,identifier names and fuunction auguments if they are required. Here is the agreement: {query}"
    return llm.complete(prompt)

def main():
    response=""
    st.title("Flow For Layman")
    st.write("This is a tool to help you generate Smart Contracts in the Cadence Language. You can use this tool to generate Smart Contracts from plain English text. ")
    col1, col2 = st.columns(2)
    with col1:
        query = st.text_input("Enter your query and hit enter")
        if query:
            with st.spinner("Please wait while we generate your response"):
                response = generate_legal_contracts(query=query)
                with col2:
                    content = st_ace(value=response,language='cdc', keybinding="vscode")
                    st.write(content)
        

        
if __name__ == "__main__":  
    main()

        # col1, col2 = st.columns(2)
    # with col1:
    #     query = st.text_input("Enter your query")
    #     if st.button("Generate Smart Contract from Legal Agreement"):
    #         with st.spinner("Please wait while we generate your response"):
    #             response = generate_legal_contracts(query=query)
    #             with col2:
    #                 content = st_ace(response)
    # if content:content

