# tutorial -->  https://www.youtube.com/watch?v=mqhxxeeTbu0

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("homepage.html")

# Otra página
@app.route("/<name>") 
def user(name):
    return f"Hello {name}" 

# redirect
@app.route("/admin")    
def admin():
    return redirect(url_for("home")) # te redirige a la homepage (def home():)

# redirect a funciones específicas con argumentos
@app.route("/admin2")    
def admin2():
    return redirect(url_for("user", name="Admin!"))   # función, nombre del parámetro = lo que quieras pasar

if __name__ == "__main__":
    app.run(debug = True)   
