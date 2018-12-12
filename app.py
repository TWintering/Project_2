from flask import Flask,render_template,redirect
from flask_pymongo import PyMongo
# import PolData
# import pymongo


app=Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/OhioDB"
mongo=PyMongo(app)




@app.route("/")
def index():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	print(senate_info)
	return render_template("index.html",senate_info=senate_info,gov_info=gov_info)


@app.route("/adams")
def adams():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("adams.html",senate_info=senate_info,gov_info=gov_info)


@app.route("/allen")
def allen():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("allen.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/ashland")
def ashland():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("ashland.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/ashtabula")
def ashtabula():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("ashtabula.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/athens")
def athens():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("athens.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/auglaize")
def auglaize():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("auglaize.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/belmont")
def belmont():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("belmont.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/brown")
def brown():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("brown.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/butler")
def butler():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("butler.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/carroll")
def carroll():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("carroll.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/champaign")
def champaign():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("champaign.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/clark")
def clark():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("clark.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/clermont")
def clermont():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("clermont.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/clinton")
def clinton():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("clinton.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/columbiana")
def columbiana():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("columbiana.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/coshocton")
def coshocton():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("coshocton.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/crawford")
def crawford():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("crawford.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/cuyahoga")
def cuyahoga():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("cuyahoga.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/darke")
def darke():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("darke.html",senate_info=senate_info,gov_info=gov_info)

@app.route("/defiance")
def defiance():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("defiance.html",senate_info=senate_info,gov_info=gov_info)
	

@app.route("/delaware")
def delaware():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("delaware.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/erie")
def erie():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("erie.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/fairfield")
def fairfield():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("fairfield.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/fayette")
def fayette():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("fayette.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/franklin")
def franklin():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("franklin.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/fulton")
def fulton():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("fulton.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/gallia")
def gallia():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("gallia.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/geauga")
def geauga():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("geauga.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/greene")
def greene():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("greene.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/guernsey")
def guernsey():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("guernsey.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/hamilton")
def hamilton():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("hamilton.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/hancock")
def hancock():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("hancock.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/hardin")
def hardin():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("hardin.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/harrison")
def harrison():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("harrison.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/henry")
def henry():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("henry.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/highland")
def highland():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("highland.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/hocking")
def hocking():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("hocking.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/holmes")
def holmes():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("holmes.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/huron")
def huron():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("huron.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/jackson")
def jackson():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("jackson.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/jefferson")
def jefferson():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("jefferson.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/knox")
def knox():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("knox.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/lake")
def lake():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("lake.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/lawrence")
def lawrence():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("lawrence.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/licking")
def licking():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("licking.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/logan")
def logan():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("logan.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/lorain")
def lorain():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("lorain.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/lucas")
def lucas():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("lucas.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/madison")
def madison():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("madison.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/mahoning")
def mahoning():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("mahoning.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/marion")
def marion():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("marion.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/medina")
def medina():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("medina.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/meigs")
def meigs():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("meigs.html",senate_info=senate_info,gov_info=gov_info)
	

@app.route("/mercer")
def mercer():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("mercer.html",senate_info=senate_info,gov_info=gov_info)
	

@app.route("/miami")
def miami():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("miami.html",senate_info=senate_info,gov_info=gov_info)
	

@app.route("/monroe")
def monroe():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("monroe.html",senate_info=senate_info,gov_info=gov_info)
	

@app.route("/montgomery")
def montgomery():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("montgomery.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/morgan")
def morgan():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("morgan.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/morrow")
def morrow():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("morrow.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/muskingum")
def muskingum():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("muskingum.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/noble")
def noble():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("noble.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/ottawa")
def ottawa():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("ottawa.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/paulding")
def paulding():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("paulding.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/perry")
def perry():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("perry.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/pickaway")
def pickaway():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("pickaway.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/pike")
def pike():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("pike.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/portage")
def portage():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("portage.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/preble")
def preble():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("preble.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/putnam")
def putnam():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("putnam.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/richland")
def richland():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("richland.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/ross")
def ross():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("ross.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/sandusky")
def sandusky():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("sandusky.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/scioto")
def scioto():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("scioto.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/seneca")
def seneca():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("seneca.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/shelby")
def shelby():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("shelby.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/stark")
def stark():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("stark.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/summit")
def summit():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("summit.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/trumbull")
def trumbull():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("trumbull.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/tuscarawas")
def tuscarawas():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("tuscarawas.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/union")
def union():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("union.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/vanwert")
def vanwert():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("vanwert.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/vinton")
def vinton():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("vinton.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/warren")
def warren():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("warren.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/washington")
def washington():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("washington.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/wayne")
def wayne():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("wayne.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/williams")
def williams():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("williams.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/wood")
def wood():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("wood.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/wyandot")
def wyandot():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("wyandot.html",senate_info=senate_info,gov_info=gov_info)
	
@app.route("/map")
def map():
	senate_info=list(mongo.db.senate.find())
	gov_info=list(mongo.db.senate.find())
	return render_template("map.html",senate_info=senate_info,gov_info=gov_info)

# @app.route("/")

# @app.route("/")

if __name__ == "__main__":
    app.run(debug=True)









