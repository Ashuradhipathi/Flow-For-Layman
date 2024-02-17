
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import os
import streamlit as st


GOOGLE_API_KEY = os.getenv("api_key")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

llm = Gemini(model="models/gemini-pro", temperature=0, embedding=GeminiEmbedding,)

def generate_smart_contract(query):
    prompt = f"\nYou are an expert in developing Smart Contracts in the Cadence Language. Use pub instead of public and generate Code for the following Smart Contract:{ query }"
    return llm.complete(prompt)

def generate_legal_contracts(query):
    prompt = f"You are an experienced Cadence Smart Contract Engineer, with extensive experience of converting legal agreements into smart contracts to be used as Ricardian contracts. Using the legal agreement below, generate a Cadence smart contract that will represent the legal agreement on the blockchain, create functions in the cntract that represents the condirions of the legal agreement. You are only required to generate the code without any explanation, you may only add comments to the codex. Here is the agreement: {query}"
    return llm.complete(prompt)

def main():
    st.title("Flow For Layman")

    st.write("This is a tool to help you generate Smart Contracts in the Cadence Language. You can use this tool to generate Smart Contracts from plain English text. You can also use this tool to convert legal agreements into smart contracts to be used as Ricardian contracts.")


    documents, legal_documents = st.tabs(['Generate Smart Contracts Using Text', 'Generate Smart Contracts Using Legal Contracts'])
    
    with documents:
        query = st.text_input("Enter the description")
        if st.button("Generate Smart Contract"):
            with st.spinner("Please wait while we generate your response"):
                response = generate_smart_contract(query=query)
                st.markdown(f"{response}", unsafe_allow_html=True)

    with legal_documents:
        query = st.text_input("Enter your query")
        if st.button("Generate Smart Contract from Legal Agreement"):
            with st.spinner("Please wait while we generate your response"):
                response = generate_legal_contracts(query=query)
                st.markdown(f"{response}", unsafe_allow_html=True)
    
        

        
if __name__ == "__main__":  
    main()

