from crypt import methods
from flask import Flask, render_template, request
import pickle
import numpy as np

# modelo de predicción
def load_model():
    with open(r"./rf_model.pkl", "rb") as archivo_entrada:
        model = pickle.load(archivo_entrada)
        # print(list_models)
    return model

app = Flask(__name__) 

# Homepage
@app.route("/", methods = ['POST', 'GET']) # ruta
def home():
    return render_template("home.html") # aquí ponemos el html con la homepage

# Página insertar datos 
@app.route("/data_input/", methods=['POST', 'GET']) # ruta
def prediction():
    return render_template("prediction.html") # aquí ponemos el html con la pg donde insertamos los datos para predicción

# Página con la predicción
@app.route('/data_input/predict/', methods=['POST']) 
def after():
    
        seasons={'spring':0, 
                'summer':1, 
                'fall':2,
                'winter':3
                }
        weathers={'clear':0, 
                    'few clouds':1, 
                    'partly cloudly':2
        }
        
        season = request.form['season']
        weather = request.form['weather']
        temp = request.form['temperature']
        humidity = request.form['humedity']
        hour = request.form['hour']
        fecha = request.form['date']
        

        year, month, day = fecha.split('-')

        data= np.array([seasons[season.lower()],weathers[weather.lower()], int(temp), int(humidity),int( year),int(month), int(day),int( hour)])
        model = load_model()
        #Hago el reshape ya que al predecir una sola instancia por fallo y error solo me ha funcionado asi
        pred= model.predict(data.reshape(1,-1))
        #EL modelo devuelve una lista, recojo la primera y unica posicion y lo redondeo al mayor para que de un numero
        final_pred= round(pred[0]) 
        print(final_pred)
        return render_template("after.html", data=int(final_pred))

# ver si host="0.0.0.0" podría solucionar problema  
if __name__ == "__main__":
    app.run(debug=False) # MUY IMPORTANTE!!!!! debug = False antes de despliegue a servidor público