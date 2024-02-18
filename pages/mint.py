from flow_config import *

class CreateCollection():
    def __init__(self, account: Address):
        self.account_address = Address.from_hex(account)
    async def run(self, ctx: Config):
        async with flow_client(
                host=ctx.access_node_host, port=ctx.access_node_port
        ) as client:
            account = await client.get_account(address=self.account_address)
            account_address = self.account_address
            new_signer =ctx.service_account_signer
            latest_block = await client.get_latest_block()
            proposer = await client.get_account_at_latest_block(
                address=account_address.bytes
            )
            transaction = Tx(
                code=open('CreateCollection.cdc').read(),
                reference_block_id=latest_block.id,
                payer=account_address,
                proposal_key=ProposalKey(
                    key_address=account_address,
                    key_id=ctx.service_account_key_id,
                    key_sequence_number=proposer.keys[0].sequence_number,
                ),
            ).add_authorizers(account_address).with_envelope_signature(
                account_address,0,new_signer,
            )

            response = await client.send_transaction(transaction=transaction.to_signed_grpc())
            transaction_id = response.id

        transaction = await client.get_transaction(id=transaction_id)
        print("transaction ID: {}".format(transaction_id.hex()))
        print("transaction payer: {}".format(transaction.payer.hex()))
        print(
            "transaction proposer: {}".format(
                transaction.proposal_key.address.hex()
            )
        )


class MintNFT():
    def __init__(self, sender: Address, receiver: Address, metadata: dict):
        self.account_address = Address.from_hex(sender)
        self.receiver_address = Address.from_hex(receiver)
        kvpair= []
        for key, value in metadata.items():
            kvpair.append(KeyValuePair(String(key), String(value)))
            
        self.metadata = Dictionary(kvpair)
    async def run(self, ctx: Config):
        async with flow_client(
                host=ctx.access_node_host, port=ctx.access_node_port
        ) as client:
            account = await client.get_account(address=self.account_address)
            account_address = self.account_address
            new_signer =ctx.service_account_signer
            latest_block = await client.get_latest_block()
            proposer = await client.get_account_at_latest_block(
                address=account_address.bytes
            )

            transaction = Tx(
                code=open("MintNFT.cdc").read(),
                reference_block_id=latest_block.id,
                payer=account_address,
                proposal_key=ProposalKey(
                    key_address=account_address,
                    key_id=0,
                    key_sequence_number=proposer.keys[0].sequence_number,
                ),
            ).add_arguments(self.receiver_address, self.metadata).add_authorizers(account_address).with_envelope_signature(
                account_address,
                0,
                new_signer,
            )

            response = await client.send_transaction(transaction=transaction.to_signed_grpc())
            transaction_id = response.id

        transaction = await client.get_transaction(id=transaction_id)
        print("transaction ID: {}".format(transaction_id.hex()))
        print("transaction payer: {}".format(transaction.payer.hex()))
        print(
            "transaction proposer: {}".format(
                transaction.proposal_key.address.hex()
            )
        )
        return transaction_id.hex()
            



class RetrieveMetadata():
    def __init__(self, receiver: Address, id: int) -> None:
        self.receiver_address = Address.from_hex(receiver)
        self.id=id

    async def run(self, ctx: Config):
        script = Script(
            code=open("ViewNFT.cdc").read(),
            arguments=[self.receiver_address, UInt64(self.id)],
        )

        async with flow_client(
            host=ctx.access_node_host, port=ctx.access_node_port
        ) as client:
            complex_script = await client.execute_script(
                script=script
                # , block_id 
                # , block_height
            )

            if not complex_script:
                raise Exception("Script execution failed")

            script_result: Value = complex_script
            m = script_result.as_type(Dictionary).value
            result = {}
            for obj in m:
                result[str(obj.key)]=str(obj.value)
            print(result)
            return result
             
class RetrieveAllNFTs():
    def __init__(self, receiver: Address) -> None:
        self.receiver_address = Address.from_hex(receiver)

    async def run(self, ctx: Config):
        script = Script(
            code=open("RetrieveAll.cdc").read(),
            arguments=[self.receiver_address],
        )

        async with flow_client(
            host=ctx.access_node_host, port=ctx.access_node_port
        ) as client:
            complex_script = await client.execute_script(
                script=script
                # , block_id 
                # , block_height
            )

            if not complex_script:
                raise Exception("Script execution failed")

            script_result: Value = complex_script
            m = script_result.as_type(Array).value
            result = []
            for obj in m:
                result.append(obj.value)
            print(result)
            return result


# a = CreateCollection('0x429b022e4a4860c5')
# asyncio.run(a.run(ctx =  Config("./flow/flow.json", 'web3hacks')))


# b = MintCert('0x429b022e4a4860c5', '0x429b022e4a4860c5', {"Name": "Moiz", "IPFS": "SFDSDFSDF"})

# asyncio.run(b.run(ctx = Config("./flow/flow.json", 'web3hacks')))

c = RetrieveAllNFTs('0x429b022e4a4860c5')
asyncio.run(c.run(ctx =  Config("./flow/flow.json", 'web3hacks')))
