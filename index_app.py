import google.generativeai 
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import os
import streamlit as st
from streamlit_ace import st_ace
from flow_config import deploy_contract
import asyncio



GOOGLE_API_KEY = os.getenv("api_key")
#
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


llm = Gemini(model="models/gemini-pro", temperature=0, embedding=GeminiEmbedding,)



def generate_legal_contracts(query):
    prompt = f"You are an experienced Cadence Smart Contract Engineer, with extensive experience of converting legal agreements into smart contracts to be used as Smart contracts. Using the legal agreement below, generate a Cadence smart contract that will represent the legal agreement on the blockchain, create functions in the cntract that represents the conditions of the legal agreement. You are only required to generate the code without any explanation, you may only add comments to the code and use proper access specifiers,identifier names and fuunction arguments if they are required.Do not include ```cadence ``` in teh response.Here is the agreement: {query}, use the {test_file} as reference"
    return llm.complete(prompt)

def main():
    check = False
    st.title("Flow For Layman")
    st.write("This is a tool to help you generate Smart Contracts in the Cadence Language. You can use this tool to generate Smart Contracts from plain English text. ")
    query = st.text_input("Enter your query and hit enter")
    if query:
        with st.spinner("Please wait while we generate your response"):
            response = generate_legal_contracts(query=query)
            check = True
        


        if check:
            st.session_state["response"] = response
            st.session_state['content'] = st.text_area(value=st.session_state["response"], label="Generated Smart Contract")
            st.markdown(f"```cadence {st.session_state['content']}```")


        st.session_state['contract_name'] = st.text_input("Enter the name of the contract")
            

        if st.session_state['contract_name']:
            st.session_state['test_contract'] = {
                        "name": st.session_state['contract_name'],
                        "source": st.session_state['content']
            }

    
        if st.button("Deploy"):
            test_contract = st.session_state['test_contract']
            contract_id = asyncio.run(deploy_contract("web3hacks",test_contract))
            st.write(f"Contract deployed successfully! Transaction ID: {contract_id}")
            

                
                    
        
        

        
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

