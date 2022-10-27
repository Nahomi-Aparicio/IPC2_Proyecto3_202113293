import re
from flask import Flask, jsonify, request
from flask_cors import CORS
import xml.etree.ElementTree as ET
from datos import XML

leei=XML()


#cd Backend flask run
#
app=Flask(__name__)
CORS(app)
#---------------------------------------------------------------------------------------------------
Dato=[{'nombre':'pan','apellido':'juan'},{'nombre':'realizado','apellido':'gato'}]

@app.route('/consultaDatos', methods=['GET'])
def obteniendoDato():
    return jsonify(Dato)


@app.route('/consultaDatos', methods=["POST"])
def creandoDato():
    body= request.get_json()

    
    apellido=body['apellido']
  

    return jsonify({'msg':'Dato agregado'})
#---------------------------------------------------------------------------------------------------
"""""@app.route('/consultaDatos', methods=['GET'])
def consultaDatos():
    return jsonify('holis datos')"""""

@app.route('/cargarDatos', methods=["POST"])
def cargarDatos():
    parse_request = request.data.decode('utf-8')
   
    leei.entrada(parse_request)
    return (parse_request)

@app.route('/cargarDatos2', methods=["POST"])
def cargarDatos2():
    parse_request2 = request.data.decode('utf-8')
   
    leei.entrada2lectu(parse_request2)
    return (parse_request2)


@app.route('/crearRecurso', methods=['POST'])
def crearRecurso():
    return jsonify('holis recursos')

@app.route('/crearCategoria', methods=['POST'])
def crearCategoria():
    return jsonify('holis recursos')


@app.route('/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    return jsonify('holis configuracion')

@app.route('/crearCliente', methods=['POST'])
def crearCliente():
    return jsonify('holis cliente')

@app.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    return jsonify('holis instancia')

@app.route('/crearFactura', methods=['POST'])
def crearFactura():
    return jsonify('holis factura')


