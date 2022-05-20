from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/glucosa")
def get_datosG():
    
    definicion = "La prueba de glucosa en la sangre mide los niveles de glucosa en la sangre. La glucosa es un tipo de azúcar. Es la principal fuente de energía del cuerpo."
    precio = 110
    return jsonify({ "definicion": definicion , "precio":precio})


if __name__ == '__main__':
    app.run(debug=True, port=4000)