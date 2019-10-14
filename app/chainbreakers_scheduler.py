import requests
from app.util import serialize_doc
from app.config import chainbreakers_api_endpoint,chainbreakers_armor_endpoint
from app import mongo
from app.config import mydb,mycursor



#--------Scheduler for fetching chainbreakers assests details--------

def chainbreakers():    
    print("running") 
    contracts = ['0x0111ac7e9425c891f935c4ce54cf16db7c14b7db']   
    for contract in contracts:
        contract_url=chainbreakers_api_endpoint.replace("{{contract}}",''+str(contract)+'')        
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
                
                ret = mongo.db.chainbreakers.update({
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



#------------Scheduler for calculating hashrate by genration,rarity,mint_number-------------

def chainbreakers_hashrate_calculation():
    print("run")
    records = mongo.db.chainbreakers.find({}, {"assetId":1})
    records = [serialize_doc(record) for record in records]
    print(records)
    for record in records:
        assetId = record['assetId']
        url=chainbreakers_armor_endpoint.replace("{{assets_id}}",''+assetId+'')
        print(url)
        response = requests.get(url=url)
        res = response.json()
        traits = res['traits']
        count = 0
        for trait in traits:
            if trait["trait_type"]=="protection":
                print("protectionnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
                protection = trait["trait_type"]
                count =count + 1 
        print(count)
        print("assetId")
        print(assetId)
        if count >= 1:
            print("adaskdsandaskdjasd")
            for trait in traits:
                if trait["trait_type"]=="generation":
                    generation_value = trait["value"]

                if trait["trait_type"]=="mint_number":
                    mint_number = trait["value"]
            genration_hashrate = 0
            if generation_value == 1:
                genration_hashrate = 30
            if generation_value == 2:
                genration_hashrate = 27.5
            mint_number_hashrate = 0
            if mint_number == 1:
                mint_number_hashrate = 20
            if mint_number == 2:
                mint_number_hashrate = 15
            if mint_number == 3:
                mint_number_hashrate = 10
            if mint_number > 4:
                mint_number_hashrate = 0

            
            hashrate = genration_hashrate + mint_number_hashrate
            print(hashrate)
            ret = mongo.db.chainbreakers.update({
                            "assetId":assetId            
                        },{
                            "$set":{
                                    "generation":generation_value,    
                                    "mint_number":mint_number,
                                    "hashrate":hashrate,
                                    "armor_type":"armor"
                            }},upsert=True)
        else:
            print("elseeeeeee")
            for trait in traits:
                if trait["trait_type"]=="generation":
                    generation_value = trait["value"]

                if trait["trait_type"]=="rarity":
                    rarity_class = trait["value"]

                if trait["trait_type"]=="mint_number":
                    mint_number = trait["value"]
            genration_hashrate = 0
            if generation_value == 0:
                genration_hashrate = 5
            if generation_value == 1:
                genration_hashrate = 2.5
            if generation_value == 2:
                genration_hashrate = 0

            rarity_hashrate = 0
            if rarity_class == "epic":
                rarity_hashrate = 30
            if rarity_class == "rare":
                rarity_hashrate = 7.5
            if rarity_class == "uncommon":
                rarity_hashrate = 5
            if rarity_class == "common":
                rarity_hashrate = 2.5
            
            mint_number_hashrate = 0
            if rarity_class == "epic" and mint_number == 1:
                mint_number_hashrate = 20
            if rarity_class == "epic" and mint_number == 2:
                mint_number_hashrate = 15
            if rarity_class == "epic" and mint_number == 3:
                mint_number_hashrate = 10
            
            if rarity_class == "rare" and mint_number == 1:
                mint_number_hashrate = 10
            if rarity_class == "rare" and mint_number == 2:
                mint_number_hashrate = 7.5
            if rarity_class == "rare" and mint_number == 3:
                mint_number_hashrate = 5
            
            if rarity_class == "uncommon" and mint_number == 1:
                mint_number_hashrate = 7.5
            if rarity_class == "uncommon" and mint_number == 2:
                mint_number_hashrate = 5
            if rarity_class == "uncommon" and mint_number == 3:
                mint_number_hashrate = 5

            if rarity_class == "common" and mint_number == 1:
                mint_number_hashrate = 5
            if rarity_class == "common" and mint_number == 2:
                mint_number_hashrate = 2.5
            if rarity_class == "common" and mint_number == 3:
                mint_number_hashrate = 2.5



            hashrate = genration_hashrate + rarity_hashrate + mint_number_hashrate
            print(hashrate)
            ret = mongo.db.chainbreakers.update({
                            "assetId":assetId            
                        },{
                            "$set":{
                                    "generation":generation_value,    
                                    "rarity_class":rarity_class,
                                    "mint_number":mint_number,
                                    "armor_type":"weapons",
                                    "hashrate":hashrate
                            }},upsert=True)
