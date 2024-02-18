import IP_NFT from 0x429b022e4a4860c5

pub fun main(account: Address, certID: UInt64) : {String: String} {

	let account = getAccount(account)
    let acctCapability = account.getCapability(IP_NFT.CollectionPublicPath)
    let receiverRef = acctCapability.borrow<&{IP_NFT.NFTReceiver}>()
        ?? panic("Could not borrow account 2 receiver reference")
    return receiverRef.getMetadata(id:certID)
}