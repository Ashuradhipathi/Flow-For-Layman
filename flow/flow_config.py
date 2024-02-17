from flow_py_sdk import flow_client, ProposalKey, Tx, Script, TransactionTemplates, cadence
import json
import logging
from pathlib import Path
import asyncio
from flow_py_sdk.cadence import Address, Dictionary, String, KeyValuePair, UInt64, Struct,Value
from flow_py_sdk.signer import InMemorySigner, HashAlgo, SignAlgo
from typing import List


log = logging.getLogger(__name__)

# 0x429b022e4a4860c5
class Config(object):
    def __init__(self, config_location: Path, acc_name) -> None:
        super().__init__()
        self.acc_name: acc_name

        self.access_node_host: str = "access.devnet.nodes.onflow.org"
        self.access_node_port: int = 9000

        self.service_account_key_id: int = 0
        
        try:
            with open(config_location) as json_file:
                data = json.load(json_file)
                self.service_account_address = Address.from_hex(
                    data["accounts"][acc_name]["address"]
                )
                self.service_account_signer = InMemorySigner(
                    hash_algo=HashAlgo.SHA3_256,
                    sign_algo=SignAlgo.ECDSA_P256,
                    private_key_hex=data["accounts"][acc_name]["key"]["privateKey"],
                )
        except Exception:
            print("exception")
            log.warning(
                f"Cannot open {config_location}, using default settings",
                exc_info=True,
                stack_info=True,
            )

async def deploy_contract(acc_name,contract):
    contract_source_hex = bytes(contract["source"], "UTF-8").hex()
    flow_acc = Config("flow.json",acc_name)

    async with flow_client(host=flow_acc.access_node_host, port=flow_acc.access_node_port) as client:
        latest_block = await client.get_latest_block()
        proposer = await client.get_account_at_latest_block(address=flow_acc.service_account_address.bytes)
        name = cadence.String(contract["name"])
        code = cadence.String(contract_source_hex)
        transaction = (
        Tx(
        code=TransactionTemplates.addAccountContractTemplate,
        reference_block_id=latest_block.id,
        payer=flow_acc.service_account_address,
        proposal_key=ProposalKey(
            key_address=flow_acc.service_account_address,
            key_id=flow_acc.service_account_key_id,
            key_sequence_number=proposer.keys[0].sequence_number,
        ),
        )
        .add_arguments(name)
        .add_arguments(code)
        .add_authorizers(flow_acc.service_account_address)
        .with_envelope_signature(
        flow_acc.service_account_address, 0, flow_acc.service_account_signer
        )  
        )
    print("Deploying contract...")
    result = await client.execute_transaction(transaction)
    print("Contract deployed successfully!")
    print("Contract ID: ", result.id.hex())
    return result.id.hex()


# test_contract = {
#     "name": "HelloWorld",
#     "source": r'''
#     pub contract HelloWorld 
#     { 
#     pub fun helloWorld(): String { 
#     return "Hello, World!" } 
#     }'''
# }
#asyncio.run(deploy_contract("web3hacks",test_contract))