from flask import (
    Blueprint,request,jsonify,abort
)
import requests
from datetime import datetime
from app.util import serialize_doc
from app.config import cryptokitties_api_endpoint
from bson.objectid import ObjectId


bp = Blueprint('fetch', __name__, url_prefix='/')
from app import mongo


'''
#------------Api for safename user 

@bp.route("/nfts",methods=["POST"])
def mons():
    if not request.json:
        abort(500)
    address=request.json.get("address", None)    
    mycryptoheroes_records = mongo.db.mycryptoheroes.find({"owner_addresses":address})
    mycryptoheroes_records = [serialize_doc(mycryptoheroes_record) for mycryptoheroes_record in mycryptoheroes_records]

    etheremon_records = mongo.db.etheremon.find({"owner_addresses":address})
    etheremon_records = [serialize_doc(etheremon_record) for etheremon_record in etheremon_records]

    cryptoskulls_records = mongo.db.cryptoskulls.find({"owner_addresses":address})
    cryptoskulls_records = [serialize_doc(cryptoskulls_record) for cryptoskulls_record in cryptoskulls_records]

    chainbreakers_records = mongo.db.chainbreakers.find({"owner_addresses":address})
    chainbreakers_records = [serialize_doc(chainbreakers_record) for chainbreakers_record in chainbreakers_records]

    cryptokitties_records = mongo.db.cryptokitties.find({"owner_addresses":address})
    cryptokitties_records = [serialize_doc(cryptokitties_record) for cryptokitties_record in cryptokitties_records]

    all_mons = mycryptoheroes_records + etheremon_records + cryptoskulls_records + chainbreakers_records + cryptokitties_records

    return jsonify({"all_mons":all_mons})
'''


@bp.route("/add_quests",methods=["POST"])
def add_quests():
    print("asdasdsadasd")
    if not request.json:
        abort(500)
    print("asdasdsada")
    quest_id = request.json.get("quest_id")
    assets = request.json.get("assets")
    trait = request.json.get("trait")
    rarity = request.json.get("rarity")
    benefits = request.json.get("benefits")
    print(quest_id,"is",assets,"as",trait,"z",rarity,"s",benefits)

    ret = mongo.db.Quests.update({
                            "quest_id":quest_id            
                        },{
                            "$set":{
                                    "quest_id":quest_id,    
                                    "asset":assets,
                                    "trait":trait,
                                    "rarity":rarity,
                                    "benefits":benefits
                            }},upsert=True)
    return jsonify({"status":"success"})



@bp.route("/delete_quests/<string:_id>",methods=["POST"])
def delete_quests(_id):
    docs = mongo.db.Quests.remove({
    "_id": ObjectId(_id)
    })
    return jsonify(str(docs))



@bp.route("/sum_of_hashrate",methods=["POST"])
def sum_of_hashrate():
    contracts = []
    address = request.json.get("address")
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
    return jsonify({"hashrate":sum_of_hashrate})