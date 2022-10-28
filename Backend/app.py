import re
from flask import Flask, jsonify, request
from flask_cors import CORS
import xml.etree.ElementTree as ET
from datos import XML
import json

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

#-------------------------------------------------------CONSULTA DATOS------------------------------------------------
@app.route('/consultandoDatos', methods=['GET'])
def obteniendoDatos():
    with open('recursosJson.json', "r") as file:
       data = json.load(file)

    with open('categoriaJson.json', "r") as file:
         data2 = json.load(file)
        
    with open('cateconfigJson.json', "r") as file:
            data3 = json.load(file)
    
    with open('clienteJSon.json', "r") as file:
       data4 = json.load(file)

    with open('instanciaJson.json', "r") as file:
         data5 = json.load(file)


    return jsonify(data,data2,data3,data4,data5)



#--------------------------------------CARGAR DATOS DEL XML------------------------------------------------------------

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

#--------------------------------------------------RECURSOS--------------------------------------------------------
@app.route('/crearRecurso', methods=['POST'])
def crearRecurso():
    body= request.get_json()
    nit=body['id']
    nombre=body['nombre']
    abreviatura=body['abreviatura']
    metrica=body['metrica']
    tipo=body['tipo']
    valorXhora=body['valorXhora']
    with open('recursosJson.json', "r") as file:
       data = json.load(file)
    data['recursos'].append({'id':nit,'nombre': nombre,'abreviatura': abreviatura,'metrica': metrica,'tipo':tipo,'valorXhora': valorXhora})
    with open('recursosJson.json', "w") as file:
         json.dump(data, file)
    Dato = {
                'message': 'Recurso agregado Exitosamente',
                'state':200
            }
    return jsonify(Dato)

@app.route('/crearRecurso', methods=['GET'])
def getRecurso():
    with open('recursosJson.json', "r") as file:
       data = json.load(file)    
    return jsonify(data)
#-----------------------------------------------------CATEGORIAS------------------------------------

@app.route('/crearCategoria', methods=['POST'])
def crearCategoria():
    body2= request.get_json()
    nit=body2['id']
    nombre=body2['nombre']
    descripcion=body2['descripcion']
    cargaTrabajo=body2['cargaTrabajo']
    with open('categoriaJson.json', "r") as file:
         data2 = json.load(file)
    data2['categoria'].append({'id':nit,'nombre': nombre,'descripcion': descripcion,'cargaTrabajo': cargaTrabajo})
    with open('categoriaJson.json', "w") as file:
            json.dump(data2, file)
    Datos = {
                'message': 'Categoria agregada Exitosamente',
                'state':200
            }
    return jsonify(Datos)
    
@app.route('/crearCategoria', methods=['GET'])
def getCategoria():
    with open('categoriaJson.json', "r") as file:
       data2 = json.load(file)    
    return jsonify(data2)

#-----------------------------------------------------CONFIGURACION------------------------------------
@app.route('/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    body3= request.get_json()
    Id=body3['ID']
    nit=body3['id']
    nombre=body3['nombre']
    descripcion=body3['descripcion']
    idRC=body3['idR']
    cantidad=body3['Recursos']
    with open('cateconfigJson.json', "r") as file:
            data3 = json.load(file)
    data3['configuracion'].append({'ID':Id,'id':nit,'nombre': nombre,'descripcion': descripcion,'idR': idRC,'Recursos':cantidad})
    with open('cateconfigJson.json', "w") as file:
            json.dump(data3, file)
    Datos = {
                'message': 'Configuracion agregada Exitosamente',
                'state':200
            }
    return jsonify(Datos)
    
@app.route('/crearConfiguracion', methods=['GET'])
def getConfiguracion():
    with open('cateconfigJson.json', "r") as file:
       data3 = json.load(file)    
    return jsonify(data3)

#-----------------------------------------------------CREARCLIENTE------------------------------------
@app.route('/crearCliente', methods=['POST'])
def crearCliente():
    body4= request.get_json()
    nit=body4['nit']
    nombre=body4['nombre']
    usuario=body4['usuario']
    direccion=body4['direccion']
    correoElectronico=body4['correoElectronico']
    with open ('clienteJSon.json', "r") as file:
        data4 = json.load(file)
    data4['cliente'].append({'nit':nit,'nombre': nombre,'usuario': usuario,'direccion': direccion,'correoElectronico': correoElectronico})
    with open('clienteJSon.json', "w") as file:
            json.dump(data4, file)
    Datos = {
                'message': 'Cliente agregado Exitosamente',
                'state':200
            }
    return jsonify(Datos)

@app.route('/crearCliente', methods=['GET'])
def getCliente():
    with open('clienteJSon.json', "r") as file:
       data4 = json.load(file)    
    return jsonify(data4)
    
#-----------------------------------------------------------------------------------------
@app.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    body5= request.get_json()
    id=body5['id']
    idConfiguracion=body5['idConfiguracion']
    nombre=body5['nombre']
    fechaInicio=body5['fechaInicio']
    estado=body5['estado']
    fechaFinal=body5['fechaFinal']
    with open ('instanciaJson.json', "r") as file:
        data5 = json.load(file)
    data5['instancia'].append({'id':id,'idConfiguracion': idConfiguracion,'nombre': nombre,'fechaInicio': fechaInicio,'estado': estado,'fechaFinal': fechaFinal})
    with open('instanciaJson.json', "w") as file:
            json.dump(data5, file)
    Datos = {
                'message': 'Instancia agregada Exitosamente',
                'state':200
            }
    return jsonify(Datos)


@app.route('/crearFactura', methods=['POST'])
def crearFactura():
    return jsonify('holis factura')


