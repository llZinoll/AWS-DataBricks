from flask import Flask, render_template, request
import pickle
import numpy as np

# modelo de predicción
def load_model():
    with open(r"\modelos\rf_model.pkl", "rb") as archivo_entrada:
        model = pickle.load(archivo_entrada)
        # print(list_models)
    return model

app = Flask(__name__)

# Homepage 
@app.route("/", methods = ["GET"]) # ruta
def index():
    return render_template("home.html") # aquí ponemos el html con la homepage

# Página insertar datos 
@app.route("/data_input/", methods=["GET"]) # ruta
def data_input():
    return render_template("prediction.html") # aquí ponemos el html con la pg donde insertamos los datos para predicción    