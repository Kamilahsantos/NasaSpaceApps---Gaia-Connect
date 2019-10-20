import mongoengine

class WeatherEvents(mongoengine.Document);

temperaturamax= mongoengine.FloatField()
temperaturamin = mongoengine.FloatField()
preciptacao = mongoengine.FloatField()
local = mongoengine.StringField()
risco = mongoengine.FloatField()
previsao = mongoengine.FloatField()
insolacao = mongoengine.FloatField(),
evaporacao_piche = mongoengine.FloatField(),
temperaturamedia = mongoengine.FloatField(),
umidaderelativa = mongoengine.FloatField(),
velocidadeVento = mongoengine.FloatField(),
timer = mongoengine.ComplexDateTimeField(),
bairro= mongoengine.StringField(),
cidade= mongoengine.StringField(),





