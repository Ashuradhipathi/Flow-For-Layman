import IP_NFT from 0x429b022e4a4860c5

transaction {
    prepare(acct: AuthAccount) {

        // Create a new empty collection
        let collection <- IP_NFT.createEmptyCollection()

        // store the empty NFT Collection in account storage
        acct.save<@IP_NFT.Collection>(<-collection, to: IP_NFT.CollectionStoragePath)

        log("Collection created for account 2")

        // create a public capability for the Collection
        acct.link<&{IP_NFT.NFTReceiver}>(IP_NFT.CollectionPublicPath, target: IP_NFT.CollectionStoragePath)

        log("Capability created")
    }
}