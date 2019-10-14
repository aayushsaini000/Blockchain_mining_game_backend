
import requests
from app.util import serialize_doc
from app.config import mycryptoheroes_api_endpoint
from app import mongo
from app.config import mydb,mycursor



#--------Scheduler for fetching mycryptoheroes assests details--------

def mycryptoheroes():    
    print("running") 
    contracts = ['0x273f7f8e6489682df756151f5525576e322d51a3']   
    for contract in contracts:
        contract_url=mycryptoheroes_api_endpoint.replace("{{contract}}",''+str(contract)+'')        
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
                name = asset['name']
                description = asset['description']
                asset_contract = asset['asset_contract']
                nftAddress = asset_contract['address']
                assetDescriptor = asset_contract['description']
                owner_addresses = asset['owner']['address']
                traits = asset['traits']
                for trait in traits:
                    #if trait['trait_type']=="rarity":
                    #    total_rarity = trait['value'] 
                    if trait['trait_type']=="lv":
                        total_level = trait['value']

                ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                                "assetId":assetId,    
                                "contract_address":nftAddress,
                                "assetDescriptor":assetDescriptor,
                                "offset":offset,
                                "image_url":image_url,
                                "owner_addresses":owner_addresses,
                                #"total_rarity":total_rarity,
                                "total_level":total_level,
                                "name":name,
                                "description":description
                        }},upsert=True)
            print(offset)



def mycryptoheroes_hashrate_calculation():
    print("mycryptoheros_run")
    records = mongo.db.mycryptoheroes.find({})
    records = [serialize_doc(record) for record in records]
    for record in records:
        assetId = record['assetId']
        total_level = record['total_level']
        total_rarity = record['total_rarity']
        if 'scarcity_rarity' in record:
            if 'scarcity_total' in record:
                scarcity_rarity = record['scarcity_rarity']
                scarcity_total = record['scarcity_total']
                if total_rarity == "Legendary":
                    rarity = 25
                if total_rarity == "Epic":
                    rarity = 15
                if total_rarity == "Rare":
                    rarity = 7.5
                if total_rarity == "Uncommon":
                    rarity = 5
                if total_rarity == "Common":
                    rarity = 2.5
                if total_rarity == "Novice":
                    rarity = 0
                

                if total_level > 0 and total_level< 49:
                    level = 0
                if total_level > 50 and total_level< 59:
                    level = 15
                if total_level > 60 and total_level< 69:
                    level = 17.5
                if total_level > 70 and total_level< 79:
                    level = 20
                if total_level > 80 and total_level< 89:
                    level = 22.5
                if total_level > 90 and total_level< 100:
                    level = 25

                hashrate = rarity+level+scarcity_rarity+scarcity_total
                print(assetId)
                print(hashrate)
                ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "hashrate":hashrate
                        }},upsert=True)
            

'''
def mycryptoheroes_scarcity_calculation():
    print("mycryptoheroes")
    class_names = ["Legendary","Epic","Rare","Uncommon","Common"]
    for class_name in class_names:
        records = mongo.db.mycryptoheroes.find({"total_rarity":class_name})
        records = [serialize_doc(record) for record in records]
        avg = len(records) / float(10)
        out = []
        last = 0.0
        while last < len(records):
            out.append(records[int(last):int(last + avg)])
            last += avg
        count = 1
        for data in out:
            for ret in data:
                assetId = ret['assetId']
                if count == 1:
                    print("111111111111111111111111111111111111")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":0
                        }},upsert=False)
                if count == 2:
                    print("222222222222222222222222222222")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":2.5
                        }},upsert=False)
                if count == 3:
                    print("33333333333333333333333333333")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":5
                        }},upsert=False)
                if count == 4:
                    print("4444444444444444444444444444444")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":7.5
                        }},upsert=False)
                if count == 5:
                    print("55555555555555555555555555555555")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":10
                        }},upsert=False)
                if count == 6:
                    print("666666666666666666666666666666")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":15
                        }},upsert=False)
                if count == 7:
                    print("777777777777777777777777777777777777")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":17.5
                        }},upsert=False)
                if count == 8:
                    print("8888888888888888888888888888888888888")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":20
                        }},upsert=False)
                if count == 9:
                    print("99999999999999999999999999999999999999999")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":22.5
                        }},upsert=False)
                if count == 10:
                    print("100000000000000000000000000000000000000000")
                    ret = mongo.db.mycryptoheroes.update({
                        "assetId":assetId            
                    },{
                        "$set":{
                            "scarcity_rarity":25
                        }},upsert=False)
            count = count + 1
'''

def mycryptoheroes_scarcity_total_calculation():
    print("mycryptoheroes")
    '''
    records = mongo.db.mycryptoheroes.find({})
    records = [serialize_doc(record) for record in records]
    different_description = []
    for record in records:
        print(record)
        if 'description' in record:
            description = record['description']
            print(description)
            if description not in different_description:
                different_description.append(description)
    count = 1
    for descrip in different_description:
        rets = mongo.db.mycryptoheroes.find({"description":descrip})
        rec = [serialize_doc(ret) for ret in rets]
        for cout in rec:
            assest = cout['assetId']
            print(assest)
            print(count)
            ret = mongo.db.mycryptoheroes.update({            
                    "assetId":assest 
                    },{
                        "$set":{
                            "count":count
                        }},upsert=True)
        count = count + 1
    '''
    returnn = mongo.db.mycryptoheroes.find().sort("count", 1)
    split = [serialize_doc(record) for record in returnn]
    avg = len(split) / float(10)
    out = []
    last = 0.0
    while last < len(split):
        out.append(split[int(last):int(last + avg)])
        last += avg
    coun = 1
    for data in out:
        for ret in data:
            assetId = ret['assetId']
            if coun == 1:
                print("111111111111111111111111111111111111")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":0
                    }},upsert=False)
            if coun == 2:
                print("222222222222222222222222222222")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":2.5
                    }},upsert=False)
            if coun == 3:
                print("33333333333333333333333333333")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":5
                    }},upsert=False)
            if coun == 4:
                print("4444444444444444444444444444444")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":7.5
                    }},upsert=False)
            if coun == 5:
                print("55555555555555555555555555555555")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":10
                    }},upsert=False)
            if coun == 6:
                print("666666666666666666666666666666")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":15
                    }},upsert=False)
            if coun == 7:
                print("777777777777777777777777777777777777")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":17.5
                    }},upsert=False)
            if coun == 8:
                print("8888888888888888888888888888888888888")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":20
                    }},upsert=False)
            if coun == 9:
                print("99999999999999999999999999999999999999999")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":22.5
                    }},upsert=False)
            if coun == 10:
                print("100000000000000000000000000000000000000000")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":25
                    }},upsert=False)
        coun = coun + 1
    
'''
def mycryptoheroes_scarcity_total_calculation():
    print("mycryptoheroes")
    records = mongo.db.mycryptoheroes.find({})
    records = [serialize_doc(record) for record in records]
    avg = len(records) / float(10)
    out = []
    last = 0.0
    while last < len(records):
        out.append(records[int(last):int(last + avg)])
        last += avg
    count = 1
    for data in out:
        for ret in data:
            assetId = ret['assetId']
            if count == 1:
                print("111111111111111111111111111111111111")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":0
                    }},upsert=False)
            if count == 2:
                print("222222222222222222222222222222")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":2.5
                    }},upsert=False)
            if count == 3:
                print("33333333333333333333333333333")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":5
                    }},upsert=False)
            if count == 4:
                print("4444444444444444444444444444444")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":7.5
                    }},upsert=False)
            if count == 5:
                print("55555555555555555555555555555555")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":10
                    }},upsert=False)
            if count == 6:
                print("666666666666666666666666666666")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":15
                    }},upsert=False)
            if count == 7:
                print("777777777777777777777777777777777777")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":17.5
                    }},upsert=False)
            if count == 8:
                print("8888888888888888888888888888888888888")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":20
                    }},upsert=False)
            if count == 9:
                print("99999999999999999999999999999999999999999")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":22.5
                    }},upsert=False)
            if count == 10:
                print("100000000000000000000000000000000000000000")
                ret = mongo.db.mycryptoheroes.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "scarcity_total":25
                    }},upsert=False)
        count = count + 1
'''