import requests
from app.util import serialize_doc
from app.config import cryptokitties_api_endpoint
from app import mongo
from app.config import mydb,mycursor



#--------Scheduler for fetching cryptokitties assests details--------

def cryptokitties():    
    print("running") 
    contracts = ['0x06012c8cf97bead5deae237070f9587f8e7a266d']   
    for contract in contracts:
        contract_url=cryptokitties_api_endpoint.replace("{{contract}}",''+str(contract)+'')        
        offset = 24001
        for off in range(1,2000):
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
                traits = asset['traits']
                print(assetId)

                exclusivity_count = 0
                fanciness_count = 0
                fancy_ranking_count = 0 
                generation_count = 0
                virginity_count = 0
                for trait in traits:
                    if trait['trait_type']=="generation":
                        generation = trait['value'] 
                        generation_count = generation_count+1
                    if trait['trait_type']=="virginity":
                        virginity = trait['value']
                        virginity_count = virginity_count+1
                    if trait['trait_type']=="exclusivity":
                        exclusivity = trait['value']
                        exclusivity_count = exclusivity_count+1
                    if trait['trait_type']=="fanciness":
                        fanciness = trait['value']
                        fanciness_count = fanciness_count+1
                    if trait['trait_type']=="fancy_ranking":
                        print("fancy_ranking")
                        fancy_ranking_count = fancy_ranking_count + 1
                        fancy_ranking = trait['value']
                
                if exclusivity_count == 1:
                    exclusivit = exclusivity
                else:
                    exclusivit = None
                if fanciness_count == 1:
                    fancines = fanciness
                else:
                    fancines = None
                if fancy_ranking_count == 1:
                    fancy_rankin = fancy_ranking
                else:
                    fancy_rankin = None
                if generation_count == 1:
                    generatio = generation
                else:
                    generatio = None
                if virginity_count == 1:
                    virginit = virginity
                else:
                    virginit = None
                    
                ret = mongo.db.cryptokitties.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                                "assetId":assetId,    
                                "contract_address":nftAddress,
                                "assetDescriptor":assetDescriptor,
                                "offset":offset,
                                "image_url":image_url,
                                "owner_addresses":owner_addresses,
                                "generation":generatio,
                                "virginity":virginit,
                                "exclusivity":exclusivit,
                                "name":name,
                                "fanciness":fancines,
                                "fancy_ranking":fancy_rankin
                        }},upsert=True)
            print(offset)



def cryptokitties_hashrate_calculation():
    print("assdajadja")
    fancyness = ["BugCat", "Lilbubthemagicspacecat", "RabbidKitty", "KnightKitty", "DracoTheMagnificent", "BugCatV2", "SirMeowsalot", "旺财汪", "Furlin"]
    comon = ["Hinecatone","Vulcant","Felono","DAPP-E"]
    Rare = ["Catbury","Catzy","PurremyAllaire"]
    assest = [1,127,251,269,282,402,500000,1000000,1500000]
    asses = [2,100]
    records = mongo.db.cryptokitties.find({})
    records = [serialize_doc(record) for record in records]
    for record in records: 
        assetId = record['assetId']
        fancy_ranking = record['fancy_ranking']
        fanciness = record['fanciness']

        if assetId in assest:
            Unique_Exclusives = 0
        else:
            Unique_Exclusives = 0
        if assetId in asses:
            Founders = 0
        else:
            Founders = 0
        if fancy_ranking == 1:
            Fancies = 0
        else:
            Fancies = 0
        if fanciness in fancyness:
            Rare_Exclusives = 0
        else:
            Rare_Exclusives = 0
        if fanciness == "Schrödingerscat":
            Schrödingerscat = 0
        else:
            Schrödingerscat = 0
        if fanciness in comon:
            Common_exclusives = 0
        else:
            Common_exclusives = 0
        if fanciness in Rare:
            Rare_fancies = 0
        else:
            Rare_fancies = 0
        hashrate = Unique_Exclusives + Founders + Fancies + Rare_Exclusives + Schrödingerscat + Common_exclusives + Rare_fancies
        print(assetId)
        ret = mongo.db.cryptokitties.update({
                "assetId":assetId            
        },{
        "$set":{
                "assetId":assetId,    
                "Unique_Exclusives":Unique_Exclusives,
                "Founders":Founders,
                "Fancies":Fancies,
                "Rare_Exclusives":Rare_Exclusives,
                "Schrödingerscat":Schrödingerscat,
                "Common_exclusives":Common_exclusives,
                "Rare_fancies":Rare_fancies,
                "hashrate":hashrate
        }},upsert=True)



