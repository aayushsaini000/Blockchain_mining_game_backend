import os
from flask import Flask,jsonify,make_response
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from app import db
mongo = db.init_db()


#----------Import schedulers functions from files----------

from app.cryptokitties_scheduler import cryptokitties,cryptokitties_hashrate_calculation
from app.cryptobeasties_scheduler import cryptobeasties,cryptobeasties_hashrate_calculation
from app.etheremon_scheduler import Etheremon,Ethermon_scarcity_calculation,Ethermon_hashrate_calculation
from app.chainbreakers_scheduler import chainbreakers,chainbreakers_hashrate_calculation
from app.mycryptoheroes_scheduler import mycryptoheroes,mycryptoheroes_hashrate_calculation,mycryptoheroes_scarcity_total_calculation #mycryptoheroes_scarcity_calculation,
from app.cryptoskulls_scheduler import cryptoskulls,cryptoskulls_hashrate_calculation
from app.chainguardians_scheduler import chainguardians
from app.quest_game_scheduler import block_winner
from app.quest_game_scheduler import winner_choose,Quest_system



#----------created app functionality----------

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()
    CORS(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify(error='Not found'), 400)

    @app.errorhandler(500)
    def error_500(error):
        return make_response({}, 500)

    db.get_db(mongo=mongo, app=app)

    from app.api import fetch

    app.register_blueprint(fetch.bp)



#----------Date time Settings of cryptokitties schedulers---------------

    cryptokitties_scheduler = BackgroundScheduler()
    cryptokitties_scheduler.add_job(cryptokitties, trigger='cron', day_of_week='mon-sat', hour=14,minute=14)
    cryptokitties_scheduler.start()

    cryptokitties_hashrate_calculation_scheduler = BackgroundScheduler()
    cryptokitties_hashrate_calculation_scheduler.add_job(cryptokitties_hashrate_calculation, trigger='cron', day_of_week='sat', hour=11,minute=32)
    cryptokitties_hashrate_calculation_scheduler.start()



#----------Date time Settings of Etheremon schedulers--------------

    etheremon_scheduler = BackgroundScheduler()
    etheremon_scheduler.add_job(Etheremon, trigger='cron', day_of_week='sat', hour=16,minute=12)
    etheremon_scheduler.start()

    Ethermon_scarcity_calculation_scheduler = BackgroundScheduler()
    Ethermon_scarcity_calculation_scheduler.add_job(Ethermon_scarcity_calculation, trigger='cron', day_of_week='sat', hour=19,minute=6)
    Ethermon_scarcity_calculation_scheduler.start()

    hashrate_calculation_scheduler = BackgroundScheduler()
    hashrate_calculation_scheduler.add_job(Ethermon_hashrate_calculation, trigger='cron', day_of_week='sat', hour=10,minute=00)
    hashrate_calculation_scheduler.start()



#-----------Date time Settings of mycryptoheroes schedulers--------------

    mycryptoheroes_scheduler = BackgroundScheduler()
    mycryptoheroes_scheduler.add_job(mycryptoheroes, trigger='cron', day_of_week='mon-sat', hour=12,minute=14)
    mycryptoheroes_scheduler.start()
    '''
    mycryptoheroes_scarcity_calculation_scheduler = BackgroundScheduler()
    mycryptoheroes_scarcity_calculation_scheduler.add_job(mycryptoheroes_scarcity_calculation, trigger='cron', day_of_week='mon-sat', hour=15,minute=40)
    mycryptoheroes_scarcity_calculation_scheduler.start()
    '''
    mycryptoheroes_hashrate_calculation_scheduler = BackgroundScheduler()
    mycryptoheroes_hashrate_calculation_scheduler.add_job(mycryptoheroes_hashrate_calculation, trigger='cron', day_of_week='mon-sat', hour=16,minute=12)
    mycryptoheroes_hashrate_calculation_scheduler.start()
    
    mycryptoheroes_scarcity_total_calculation_scheduler = BackgroundScheduler()
    mycryptoheroes_scarcity_total_calculation_scheduler.add_job(mycryptoheroes_scarcity_total_calculation, trigger='cron', day_of_week='mon-sat', hour=14,minute=20)
    mycryptoheroes_scarcity_total_calculation_scheduler.start()
    


#-----------Date time Settings of mycryptoheroes schedulers---------------

    chainbreakers_scheduler = BackgroundScheduler()
    chainbreakers_scheduler.add_job(chainbreakers, trigger='cron', day_of_week='sat', hour=19,minute=11)
    chainbreakers_scheduler.start()


    chainbreakers_hashrate_calculation_scheduler = BackgroundScheduler()
    chainbreakers_hashrate_calculation_scheduler.add_job(chainbreakers_hashrate_calculation, trigger='cron', day_of_week='mon-sat', hour=13,minute=21)
    chainbreakers_hashrate_calculation_scheduler.start()



#-----------Date time Settings of cryptobeasties schedulers----------------

    cryptobeasties_scheduler = BackgroundScheduler()
    cryptobeasties_scheduler.add_job(cryptobeasties, trigger='cron', day_of_week='sat', hour=15,minute=5)
    cryptobeasties_scheduler.start()

    cryptobeasties_hashrate_calculation_scheduler = BackgroundScheduler()
    cryptobeasties_hashrate_calculation_scheduler.add_job(cryptobeasties_hashrate_calculation, trigger='cron', day_of_week='sat', hour=10,minute=18)
    cryptobeasties_hashrate_calculation_scheduler.start()



#-----------Date time Settings of cryptoskulls schedulers---------------

    cryptoskulls_scheduler = BackgroundScheduler()
    cryptoskulls_scheduler.add_job(cryptoskulls, trigger='cron', day_of_week='sat', hour=14,minute=55)
    cryptoskulls_scheduler.start()



    cryptoskulls_hashrate_calculation_scheduler = BackgroundScheduler()
    cryptoskulls_hashrate_calculation_scheduler.add_job(cryptoskulls_hashrate_calculation, trigger='cron', day_of_week='sat', hour=11,minute=25)
    cryptoskulls_hashrate_calculation_scheduler.start()



#-----------Date time Settings of chainguardians schedulers--------------

    chainguardians_scheduler = BackgroundScheduler()
    chainguardians_scheduler.add_job(chainguardians, trigger='cron', day_of_week='sat', hour=11,minute=30)
    chainguardians_scheduler.start()



#-----------scheduler for block winner--------------

    block_winner_scheduler = BackgroundScheduler()
    block_winner_scheduler.add_job(block_winner, trigger='cron', day_of_week='sat', hour=18,minute=24)
    block_winner_scheduler.start()



#-----------scheduler for block winner--------------

    winner_choose_scheduler = BackgroundScheduler()
    winner_choose_scheduler.add_job(winner_choose, trigger='interval', minutes =120)
    winner_choose_scheduler.start()


#-----------Scheduler for Quest System------------

    Quest_system_scheduler = BackgroundScheduler()
    Quest_system_scheduler.add_job(Quest_system, trigger='cron', day_of_week='sat', hour=16,minute=28)
    Quest_system_scheduler.start()



    try:
        return app
    except:
        cryptokitties_scheduler.shutdown()
        etheremon_scheduler.shutdown()
        mycryptoheroes_scheduler.shutdown()
        chainbreakers_scheduler.shutdown()
        cryptoskulls_scheduler.shutdown()
        cryptobeasties_scheduler.shutdown()
        chainguardians_scheduler.shutdown()
        chainbreakers_hashrate_calculation_scheduler.shutdown()
        cryptoskulls_hashrate_calculation_scheduler.shutdown()
        #mycryptoheroes_scarcity_calculation_scheduler.shutdown()
        mycryptoheroes_hashrate_calculation_scheduler.shutdown()
        mycryptoheroes_scarcity_total_calculation_scheduler.shutdown()
        Ethermon_scarcity_calculation_scheduler.shutdown()
        hashrate_calculation_scheduler.shutdown()
        block_winner_scheduler.shutdown()
        winner_choose_scheduler.shutdown()
        cryptobeasties_hashrate_calculation_scheduler.shutdown()
        Quest_system_scheduler.shutdown()