from flask import Flask
app = Flask(__name__)
#con esto se importa mi archivo de python donde estan las vistas
from app import views