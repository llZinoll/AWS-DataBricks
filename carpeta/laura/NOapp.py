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
    return render_template("homepage.html") # aquí ponemos el html con la homepage

# Página insertar datos 
@app.route("/data_input/", methods=["GET"]) # ruta
def data_input():
    return render_template("data_page.html") # aquí ponemos el html con la pg donde insertamos los datos para predicción

# Página con la predicción
@app.route('/data_input/predict/', methods=['POST']) 
def predict():
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
        temp = request.form['temp']
        humidity = request.form['humidity']
        date = request.form['date']
        hour = request.form['hour']

        year, month, day = date.split('-')

        data= np.array([seasons[season.lower()],weathers[weather.lower()], int(temp), int(humidity),int( year),int(month), int(day),int( hour)])
        model = load_model()
        #Hago el reshape ya que al predecir una sola instancia por fallo y error solo me ha funcionado asi
        pred= model.predict(data.reshape(1,-1))
        #EL modelo devuelve una lista, recojo la primera y unica posicion y lo redondeo al mayor para que de un numero
        final_pred= round(pred[0]) 
        return render_template('predict.html', data=int(final_pred))
  
if __name__ == "__main__":
    app.run(debug=True) # MUY IMPORTANTE!!!!! debug = False antes de despliegue a servidor público