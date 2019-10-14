import requests
from app.util import serialize_doc
from app import mongo
from app.config import mydb,mycursor
import random
import datetime

#--------Scheduler for quest gaming block winner--------

def block_winner():
    print("running block")
    recor = mongo.db.hashrate_calculation.remove()
    mycursor.execute('SELECT username FROM sws_user')
    check = mycursor.fetchall()
    count=1
    for user in check:
        username=user[0]
        mycursor.execute('SELECT address from sws_address WHERE cms_login_name="'+str(username)+'" ') 
        chek = mycursor.fetchall()
        contracts = []
        for addr in chek:
            address=addr[0]
            print("addressssssssssssssssssssssssssss")
            print(address)
            heroes_records = mongo.db.participate_heroes.find_one({"address":address})
            chain = heroes_records['chainbreakers']
            crypto = heroes_records['cryptoskulls']
            ethere = heroes_records['etheremon']
            mycrypto = heroes_records['mycryptoheroes']

            mycryptoheroes_records = mongo.db.mycryptoheroes.find({"owner_addresses":address})
            mycryptoheroes_records = [serialize_doc(mycryptoheroes_record) for mycryptoheroes_record in mycryptoheroes_records]
            mycryptoheroes_rec = mycryptoheroes_records[0:1]

            etheremon_records = mongo.db.etheremon.find({"owner_addresses":address})
            etheremon_records = [serialize_doc(etheremon_record) for etheremon_record in etheremon_records]
            etheremon_rec = etheremon_records[0:1]

            cryptoskulls_records = mongo.db.cryptoskulls.find({"owner_addresses":address})
            cryptoskulls_records = [serialize_doc(cryptoskulls_record) for cryptoskulls_record in cryptoskulls_records]
            cryptoskulls_rec = cryptoskulls_records[0:1]

            chainbreakers_records = mongo.db.chainbreakers.find({"owner_addresses":address})
            chainbreakers_records = [serialize_doc(chainbreakers_record) for chainbreakers_record in chainbreakers_records]
            chainbreakers_rec = chainbreakers_records[0:1]

            all_mons = mycryptoheroes_rec + etheremon_rec + cryptoskulls_rec + chainbreakers_rec #+ cryptokitties_records
            
            for mons in all_mons:
                contracts.append(mons)
        print("4")
        user_hashrate_sum = []
        for all_contracts in contracts:
            if 'hashrate' in all_contracts:
                hashrate = all_contracts['hashrate']            
                user_hashrate_sum.append(hashrate)
        print("4777777")
        sum_of_hashrate=sum(user_hashrate_sum)
        print(len(user_hashrate_sum))
        print("499999999")
        print(sum_of_hashrate)
        
        if count == 1:
            print("5111111111111111111111111")
            starting_number = 1 
            ending_number = starting_number + sum_of_hashrate
        else:
            print("55555555555555555555555555555555")
            highest = mongo.db.hashrate_calculation.find_one(sort=[("ending_number", -1)])
            print("6000000000000000")
            print(highest)
            print("6222222222222222")
            if highest is not None:
                starting_number = highest['ending_number']
                ending_number = sum_of_hashrate + starting_number
                print(starting_number)
                print(ending_number)
            else:
                starting_number = None
                ending_number = None
        count = count + 1
        print("71111111111111")
        ret = mongo.db.hashrate_calculation.update({
                        "username":username            
                    },{
                        "$set":{
                                "username":username,    
                                "sum_of_hashrate":sum_of_hashrate,
                                "starting_number":starting_number,
                                "ending_number":ending_number
                        }},upsert=True)
        print("doneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")



def winner_choose():
    print("running")   
    highest = mongo.db.hashrate_calculation.find_one(sort=[("ending_number", -1)])
    highest_number = highest['ending_number']
    random_number = random.randint(1,int(highest_number))
    hashrate_records = mongo.db.hashrate_calculation.find({ "sum_of_hashrate": {"$ne":0}})
    hashrate_records = [serialize_doc(hashrate_record) for hashrate_record in hashrate_records]
    winner_array = []
    print(random_number)
    for check in hashrate_records:
        username = check['username']
        starting_number = check['starting_number']
        ending_number = check['ending_number']
        winner_checking=range(starting_number,ending_number)
        if random_number in winner_checking:
            winner_array.append(username)
        else:
            pass
    winner = winner_array[0]
    max_block = mongo.db.winner_block.find_one(sort=[("Block_Number", -1)])
    if max_block is not None:
        block = max_block["Block_Number"]
        block_number = block + 1
    else:
        block_number = 1
    block_insert = mongo.db.winner_block.insert_one({
        "Miner": winner,
        "Block_Number":block_number,
        "Difficulty":20,
        "TimeStamp":datetime.datetime.utcnow(),
        "Rewards_Type":"CGC",
        "Reward_Amount":25
    }).inserted_id 



def Quest_system():
    blocks = mongo.db.User_quests.find({})
    blocks = [serialize_doc(block) for block in blocks]
    for block in blocks:
        print("asdasda")
