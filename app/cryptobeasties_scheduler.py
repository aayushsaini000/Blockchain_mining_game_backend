
import requests
from app.util import serialize_doc
from app.config import cryptobeasties_api_endpoint
from app import mongo
from app.config import mydb,mycursor



#--------Scheduler for fetching cryptobeasties assests details--------

def cryptobeasties():    
    print("cryptobeasties") 
    contracts = ['0xffdf17652cca46eb98a214cb3e413c8661241e49']   
    for contract in contracts:
        contract_url=cryptobeasties_api_endpoint.replace("{{contract}}",''+str(contract)+'')        
        offset = 1
        for off in range(1,1000):
            assets_url=contract_url.replace("{{offset}}",''+str(offset)+'')
            assets = requests.get(url=assets_url)   #name : "Light Fighter #11290"
            response = assets.json()      
            assets_data = response['assets']
            offset = offset + 250
            for asset in assets_data:
                assetId = asset['token_id']
                image_url=asset['image_url']
                name = asset['name']
                asset_contract = asset['asset_contract']
                nftAddress = asset_contract['address']
                assetDescriptor = asset_contract['description']
                owner_addresses = asset['owner']['address']
                traits = asset['traits']
                for trait in traits:
                    if trait['trait_type']=="rarity":
                        rarity = trait['value'] 
                    if trait['trait_type']=="badge":
                        badge = trait['value']
                    if trait['trait_type']=="level_Num":
                        level_Num = trait['value']


                ret = mongo.db.cryptobeasties.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                                "assetId":assetId,    
                                "contract_address":nftAddress,
                                "assetDescriptor":assetDescriptor,
                                "offset":offset,
                                "image_url":image_url,
                                "owner_addresses":owner_addresses,
                                "rarity":rarity,
                                "badge":badge,
                                "level_Num":level_Num,
                                "name":name
                        }},upsert=True)
            print(offset)



def cryptobeasties_hashrate_calculation():    
    print("cryptobeasties hashrate calculations")
    records = mongo.db.cryptobeasties.find({})
    records = [serialize_doc(record) for record in records]
    for recor in records:
        assetId = recor['assetId']
        rarity = recor['rarity']
        badge = recor['badge']
        level_Num = recor['level_Num']
        if rarity == "Common":
            rarity_hash = 5
        if rarity == "Uncommon":
            rarity_hash = 10
        if rarity == "Rare":
            rarity_hash = 15
        if rarity == "Epic":
            rarity_hash = 25
        if rarity == "Legendary":
            rarity_hash = 40
        if rarity == "Phenomenal":
            rarity_hash = 60
        
        if level_Num >= 30:
            Evolved = True
        if level_Num < 30:
            Evolved = False
        
        hashrate = rarity_hash
        print(assetId)
        ret = mongo.db.cryptobeasties.update({
                "assetId":assetId            
            },{
                "$set":{
                        "assetId":assetId,    
                        "rarity_hash":rarity_hash,
                        "Evolved":Evolved,
                        "hashrate":hashrate
                }},upsert=True)
                
        