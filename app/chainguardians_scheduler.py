
import requests
from app.util import serialize_doc
from app.config import chainguardians_api_endpoint
from app import mongo
from app.config import mydb,mycursor



#--------Scheduler for fetching chainguardians assests details--------

def chainguardians():    
    print("chainguardians") 
    contracts = ['0x3cd41ec039c1f2dd1f76144bb3722e7b503f50ab']   
    for contract in contracts:
        contract_url=chainguardians_api_endpoint.replace("{{contract}}",''+str(contract)+'')        
        offset = 1
        for off in range(1,1000):
            assets_url=contract_url.replace("{{offset}}",''+str(offset)+'')
            assets = requests.get(url=assets_url)
            response = assets.json()      
            assets_data = response['assets']
            offset = offset + 250
            for asset in assets_data:
                assetId = asset['token_id']
                image_url=asset['image_url']
                asset_contract = asset['asset_contract']
                nftAddress = asset_contract['address']
                assetDescriptor = asset_contract['description']
                owner_addresses = asset['owner']['address']
                traits = asset['traits']
                for trait in traits:
                    if trait['trait_type']=="class_name":
                        class_name = trait['value'] 
                    if trait['trait_type']=="level":
                        total_level = trait['value']
                    if trait['trait_type']=="catch_number":
                        catch_index = trait['value']

                ret = mongo.db.chainguardians.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                                "assetId":assetId,    
                                "contract_address":nftAddress,
                                "assetDescriptor":assetDescriptor,
                                "offset":offset,
                                "image_url":image_url,
                                "owner_addresses":owner_addresses,
                                "class_name":class_name,
                                "total_level":total_level,
                                "catch_index":catch_index,
                                "name":"chainguardians"
                        }},upsert=True)
            print(offset)
