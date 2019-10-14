import requests
from app.util import serialize_doc
from app.config import cryptoskulls_api_endpoint,cryptoskull_hashrate_endpoint
from app import mongo
from app.config import mydb,mycursor





#--------Scheduler for fetching cryptoskulls assests details--------

def cryptoskulls():    
    print("cryptoskulls") 
    contracts = ['0xc1caf0c19a8ac28c41fe59ba6c754e4b9bd54de9']   
    for contract in contracts:
        contract_url=cryptoskulls_api_endpoint.replace("{{contract}}",''+str(contract)+'')        
        offset = 1
        for off in range(1,100):
            assets_url=contract_url.replace("{{offset}}",''+str(offset)+'')
            assets = requests.get(url=assets_url)
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

                ret = mongo.db.cryptoskulls.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                                "assetId":assetId,    
                                "contract_address":nftAddress,
                                "assetDescriptor":assetDescriptor,
                                "offset":offset,
                                "image_url":image_url,
                                "owner_addresses":owner_addresses,            
                                "name":name
                        }},upsert=True)
            print(offset)




#--------Scheduler for cryptoskulls assests hashrate details calculation--------


def cryptoskulls_hashrate_calculation():
    print("crypto run")
    records = mongo.db.cryptoskulls.find({"name":"cryptoskulls"}, {"assetId":1})
    records = [serialize_doc(record) for record in records]
    for record in records:
        assetId = record['assetId']
        url=cryptoskull_hashrate_endpoint.replace("{{assets_id}}",''+assetId+'')
        response = requests.get(url=url)
        res = response.json()
        hashrate = res['hashrate']     
        print(hashrate)
        print(assetId)        
        ret = mongo.db.cryptoskulls.update({
                "assetId":assetId            
            },{
                "$set":{
                        "hashrate":hashrate,   
                }},upsert=True)
