import pymysql


#

#mydb = pymysql.connect(host='198.38.93.150',user='dexter',password='cafe@wales1',database='db_safename')
mydb = pymysql.connect(user="VsaqpBhCxL" , password="sW9BgYhqmG", host="remotemysql.com", database="VsaqpBhCxL")
mycursor=mydb.cursor()


#mydb = pymysql.connect(host='198.38.93.150',user='dexter',password='cafe@wales1',database='db_safename')
#mydb = pymysql.connect(user="VsaqpBhCxL" , password="sW9BgYhqmG", host="remotemysql.com", database="VsaqpBhCxL")


#----------Database MongoUri-----------

MongoUri ="mongodb+srv://root:wN4MDrm1jSiyzDQk@cluster0-v8o7t.mongodb.net/chainguardians?retryWrites=true&w=majority"
#"mongodb+srv://xmage:xmage@cluster0-xooqb.mongodb.net/chainguardians?retryWrites=true"
#"mongodb+srv://xmage:xmage@cluster0-xooqb.mongodb.net/chainguardians?retryWrites=true"
#"mongodb+srv://chaingardians:rasealex@cluster0-xooqb.mongodb.net/chainguardians?retryWrites=true&w=majority"
#mongodb+srv://snake:gardians@cluster0-v8o7t.mongodb.net/test?retryWrites=true&w=majority


chainbreakers_armor_endpoint = "https://api.opensea.io/asset/0x0111ac7e9425c891f935c4ce54cf16db7c14b7db/{{assets_id}}/"
cryptoskull_hashrate_endpoint = "https://cryptoskulls.com/api/hashrate/{{assets_id}}"


#----------Nonfungible Apis end points------------

cryptokitties_api_endpoint="https://api.opensea.io/api/v1/assets/?asset_contract_address={{contract}}&offset={{offset}}&limit=250"
etheremon_api_endpoint="https://api.opensea.io/api/v1/assets/?asset_contract_address={{contract}}&offset={{offset}}&limit=250"
mycryptoheroes_api_endpoint="https://api.opensea.io/api/v1/assets/?asset_contract_address={{contract}}&offset={{offset}}&limit=250"
chainbreakers_api_endpoint="https://api.opensea.io/api/v1/assets/?asset_contract_address={{contract}}&offset={{offset}}&limit=250"
cryptobeasties_api_endpoint="https://api.opensea.io/api/v1/assets/?asset_contract_address={{contract}}&offset={{offset}}&limit=250"
cryptoskulls_api_endpoint="https://api.opensea.io/api/v1/assets/?asset_contract_address={{contract}}&offset={{offset}}&limit=250"
chainguardians_api_endpoint="https://api.opensea.io/api/v1/assets/?asset_contract_address={{contract}}&offset={{offset}}&limit=250"



mon_names = ['Dilloom','Dynamouse','Nageel','Eekape','Palytid','Mianari','Berrball','Cesstoid','Mizumi','Chulember','Blockid','Thermolophus','Keradon',
                    'Vermillios','Vivorin','Windora','Geenee','Quillster','Baulder','Vibe','Swifty','Pangrass','Mintol','Omnom','Kyari','Lectrobe','Mirrie','Cobrus',
                    'Lollipunch','Odwig','Tygloo','Pudde','Mushmite','Polynimo','Fuirrel','Dillow','Pyrode','Moranagi','Moldec','Oculid','Surinari',
                    'Silvyx','Coronoid','Watadzumi','Fuenago','Geckelic','Blockall','Geerex','Dredrock','Florost','Yumee','Candeliria','Wrektric',
                    'Reflectre','Dracobra','Mawverize','Occlusk','Mechloo','Aquary','Squake','Qairrel','Dillossus','Raxplode','Dehedra','Aphroxid',
                    'Tekagon','Aromerita','Liscious','Resurvy','Morinori','Gremin','Spoxin','Intelix','Lilspri','Inkami','Redhandit','Endorr','Sonectid',
                    'Cryptise','Tenteink','Criminiac','Endrowth','Nuklectid','Cremortus','Monstratos','Duscre','Mapla','Barkindle','Wolflaze','Wolverize','Ruffski','Arblizen',
                    'Siberizen','Tundrill','Matara','Matarama','Malakel’E','Kahukel’E','Tobeno','Puremu','Flaraton','Inferacoon','Scubella','Ekopi','Ekoraft','Expertri',
                    'Purgast','Smeltal','Vorvosip','Devostoric','Sauntler','Zapillar','Infiluv','Krubble','Krabboul','Capareef','Tipsillar','Mesmerhys','Chromothic','Grubgas',
                    'Polupa','Noxibeet','Kelpony','Chevalage','Reefallion','Lemeeni','Lemeeglar','Primasham','Iquander','Iquanaze','Wrecktile','Mindallion','Talisment','Krakowee','Ribibrawl',
                    'Vexigon','Noxareo','Darcastro','Greipawn','Vitisir','Vernirox','Quadrossal','Zedakazm','Armadigoal','Armordigoal','Pangrove','Kyberra','Kyberram',
                    'Pigperus','Boarazer','Piggicius','Wartoink']



