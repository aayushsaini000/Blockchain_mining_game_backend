
import requests
from app.util import serialize_doc
from app.config import etheremon_api_endpoint
from app import mongo
from app.config import mydb,mycursor,mon_names






#--------Scheduler for fetching Etheremon assests details--------

def Etheremon():    
    print("running") 
    contracts = ['0x5d00d312e171be5342067c09bae883f9bcb2003b']   
    for contract in contracts:
        contract_url=etheremon_api_endpoint.replace("{{contract}}",''+str(contract)+'')        
        offset = 1
        for off in range(500,1000):
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
                for trait in traits:
                    if trait['trait_type']=="class_name":
                        class_name = trait['value'] 
                    if trait['trait_type']=="level":
                        total_level = trait['value']
                    if trait['trait_type']=="catch_number":
                        catch_index = trait['value']

                ret = mongo.db.etheremon.update({
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
                                "name":name
                        }},upsert=True)
            print(offset)







#------------Scheduler for ethermon scarcity---------------

def Ethermon_scarcity_calculation():
    class_names = mon_names
    uncommon_scarity = ["Wolverize","Siberizen","Tekagon","Quadrossal","Vernirox","Zedakazm","Baulder","Barkindle","Ruffski"]
    for class_name in class_names:
        if class_name in uncommon_scarity:
            records = mongo.db.etheremon.find({"class_name":class_name})
            records = [serialize_doc(record) for record in records]
            for recor in records:
                classs = recor['class_name']
                assetId = recor['assetId']
                ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                        },{
                            "$set":{
                                "scarcity":25
                            }},upsert=False)

        else:    
            common_scarity = ["Pangrove","Darcastro","Wrecktile","Primasham","Reefallion","Noxibeet","Chromothic","Capareef","Expertri","Duscre","Monstratos",
                    "Resurvy","Liscious","Aromerita","Aphroxid","Dehedra","Raxplode","Dillossus","Qairrel"]
            records = mongo.db.etheremon.find({"class_name":class_name})
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
                    classs = ret['class_name']
                    if count == 1:
                        print("111111111111111111111111111111111111")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":1 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                                },{
                                "$set":{
                                    "scarcity":1
                                }},upsert=False)
                    if count == 2:
                        print("222222222222222222222222222222")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":2 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":2
                                }},upsert=False)
                    if count == 3:
                        print("33333333333333333333333333333")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":3 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":3
                                }},upsert=False)
                    if count == 4:
                        print("4444444444444444444444444444444")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":4 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":4
                                }},upsert=False)
                    if count == 5:
                        print("55555555555555555555555555555555")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":5 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":5
                                }},upsert=False)
                    if count == 6:
                        print("666666666666666666666666666666")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":6 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":6
                                }},upsert=False)
                    if count == 7:
                        print("777777777777777777777777777777777777")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":7 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":7
                                }},upsert=False)
                    if count == 8:
                        print("8888888888888888888888888888888888888")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":8 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":8
                                }},upsert=False)
                    if count == 9:
                        print("99999999999999999999999999999999999999999")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":9 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":9
                                }},upsert=False)
                    if count == 10:
                        print("100000000000000000000000000000000000000000")
                        if classs in common_scarity:
                            ret = mongo.db.etheremon.update({
                            "assetId":assetId            
                            },{
                            "$set":{
                                "scarcity":10 + 10
                            }},upsert=False)
                        else:
                            ret = mongo.db.etheremon.update({
                                "assetId":assetId            
                            },{
                                "$set":{
                                    "scarcity":10
                                }},upsert=False)
                count = count + 1



#-------Etheremon hashrate calculation
                
                
def Ethermon_hashrate_calculation():
    print("run")
    records = mongo.db.etheremon.find({"name":"etheremon"})
    records = [serialize_doc(record) for record in records]
    for record in records:
        total_level = record['total_level']
        catch_index = record['catch_index']
        if 'scarcity' in record:
            scarcity_hashrate = record['scarcity']
            assetId = record['assetId']
            if total_level < 39:
                level_hashrate = 0
            if total_level > 40 and total_level < 59:
                level_hashrate = 10
            if total_level > 60 and total_level < 79:
                level_hashrate = 15
            if total_level > 80 and total_level < 89:
                level_hashrate = 20
            if total_level > 90 and total_level < 99:
                level_hashrate = 22.5    
            if total_level == 100:
                level_hashrate = 25

            if catch_index == 1 :
                catch_hashrate = 25
            if catch_index == 2 :
                catch_hashrate = 20
            if catch_index == 3:
                catch_hashrate = 15
            else:
                catch_hashrate = 0
            hashrate = level_hashrate + catch_hashrate + scarcity_hashrate
            print(assetId)
            ret = mongo.db.etheremon.update({
                    "assetId":assetId            
                },{
                    "$set":{
                        "hashrate":hashrate
                    }},upsert=True)

