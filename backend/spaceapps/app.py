from flask import Flask
from bson.json_util import dumps
import pymongo 
from pymongo import MongoClient
from flask import request
from bson.json_util import dumps
import json
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import dns
import ast
import imp
from model import NLPModel


model=open('C:/Users/kamilasantos/Downloads/gaia_previsao_chuva.pkl','rb')
 
client = pymongo.MongoClient('import pymongo')
 
helper_module = imp.load_source('*', 'C:/Users/kamilasantos/nasaspaceapps/backend/spaceapps/helper.py')
model = NLPModel()

client = pymongo.MongoClient("mongodb+srv://spaceapps:<spaceapps>@cluster0-jf6fr.mongodb.net/test?retryWrites=true&w=majority") 
db = client.ContactDB
collection = db['WeatherEvents']

app = Flask(__name__)
api = Api(app)


#library pkl
clf_path = 'lib/models/SentimentClassifier.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

#carregar vetor
vec_path = 'lib/models/TFIDFVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)

parser = reqparse.RequestParser()
parser.add_argument('query')


@app.route("/")
def home():

        data= json.loads(request.data)
        Id= data['Id']
        Temperaturamax= data['temperaturamax'],
        TemperaturaMin = data['temperaturamin'],
        Preciptacao = data['preciptacao'],
        Local = data['local'],
        Risco= data['risco'],
        Previsao = data['previsao'],
        Insolacao = data['insolacao'],
        Evaporacao_Piche =data ['evaporacao_piche'],
        Temperaturamedia=  data ['temperaturamedia'],
        UmidadeRelativa = data ['umidaderelativa'],
        VelocidadeVento = data ['velocidadeVento'],
        Timer = data ['timer'],
        Bairro = data['bairro'],

@app.route("/district", methods = ['GET'])
def get_district():
    print ("pagina com todas as cidades")

    try:
        #lista todos os eventos climáticos que ocorreram nos distrtitos cadastrados
        return dumps(WeatherEvents)
        resp.status_code = 200

    except  e:
        return not_found()
    if collection.find().count > 0:
        return dumps(collection.find())
    else:
            return jsonify([])



@app.route("/district/<page_id>", methods = ['GET'])
def FindById():
    print ("busca as cidades por id")

    try:
        district = [district for district in district if district['id'] == district_id]
        WeatherEvents= db.WeatherEvents.find(Id)
        return dumps(WeatherEvents)

       
    except e:
        return not_found()

    data = json.loads(request.data)
    WeatherEvents = data['WeatherEvents']  

