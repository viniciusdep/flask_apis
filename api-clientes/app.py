from flask import Flask
from flask_cors import CORS, cross_origin 
from prometheus_flask_exporter import PrometheusMetrics
#CORS é um descorador de rotas, podemos passar parametros de metodos ou atenticação
#Exemplo: flask_cors. cross_origin ( origins = "/", methods = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT']


app = Flask(__name__)
metrics = PrometheusMetrics(app)
CORS(app)