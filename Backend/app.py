
import webbrowser
from flask import Flask, jsonify, request,Response
from flask_cors import CORS
import xml.etree.ElementTree as ET
from datos import XML
import json
from Factura import haciendoFact

leei=XML()
factu=haciendoFact()


#cd Backend flask run
#
app=Flask(__name__)
CORS(app)
cors=CORS(app, resources={r"/*": {"origins": "*"}})

#---------------------------------------------------------------------------------------------------
"""Dato=[{'nombre':'pan','apellido':'juan'},{'nombre':'realizado','apellido':'gato'}]

@app.route('/consultaDatos', methods=['GET'])
def obteniendoDato():
    return jsonify()


@app.route('/consultaDatos', methods=["POST"])
def creandoDato():
    body= request.get_json()
    apellido=body['apellido']
    return jsonify({'msg':'Dato agregado'})"""

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
    parse_request = request.data.decode('utf-8')  #configuracion.xml  
    leei.entrada(parse_request)   
    dato={'msg':'Datos cargados'}    
    return jsonify(dato)

@app.route('/cargarDatos', methods=['GET'])
def potDatos():
    b=leei.getContCli()
    c=leei.getContInst()
    d=leei.getContRe()    
    if b==0 and c==0 and d==0:
        datos="no existen  datos"
    else:
        datos="archivo subido correctamente\n"
        datos+="se cargaron "+str(b)+" clientes\n"
        datos+="se cargaron "+str(c)+" instancias\n"
        datos+="se cargaron "+str(d)+" recursos\n"
        print(datos)
    return Response(datos)
"""
@app.route('/cargarDatos', methods=['GET'])
def cargarDatos():
    dato={'msg':'Datos cargados'}  
    return jsonify(dato)    """
    

@app.route('/cargarDatos2', methods=["POST"])
def cargarDatos2():
    parse_request2 = request.data.decode('utf-8')
    leei.entrada2lectu(parse_request2)
    dato={'msg':'Datos cargados'}    
    return jsonify(dato)

@app.route('/cargarDatos2', methods=['GET'])
def potDatos2():
    b=leei.getConsum()
    if b==0:
        datos="no existen consumos"
    else:
        datos="archivo subido correctamente\n"
        datos+="se cargaron "+str(b)+" consumos\n"
        print(datos)
    return Response(datos)

"""
@app.route('/crearFactura', methods=['GET'])
def getcrearFactura():
    dato={'msg':'Datos cargados'}  
    return jsonify(dato)    """


#--------------------------------------------------RECURSOS--------------------------------------------------------
@app.route('/crearRecurso', methods=['POST'])
def crearRecurso():
    """"
    body= request.get_json()
    
    id=body['id']
    
    nombre=body['nombre']
    abreviatura=body['abreviatura']
    metrica=body['metrica']
    tipo=body['tipo']
    valorXhora=body['valorXhora']"""

    lista=request.data.decode('utf-8') #si lo pongo como Json F todo 
    conver=lista.split(',')
    id=str(conver[0])
    nombre=str(conver[1])
    abreviatura=str(conver[2])
    metrica=str(conver[3])
    tipo=str(conver[4])
    valorXhora=str(conver[5])
    print(id)

    print(id,nombre,abreviatura,metrica,tipo,valorXhora)
    print(id,nombre,abreviatura,metrica,tipo,valorXhora)
    with open('recursosJson.json', "r") as file:
       data = json.load(file)
    data['recursos'].append({'id':id,'nombre': nombre,'abreviatura': abreviatura,'metrica': metrica,'tipo':tipo,'valorXhora': valorXhora})
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
    return Response(data)
#-----------------------------------------------------CATEGORIAS------------------------------------

@app.route('/crearCategoria', methods=['POST'])
def crearCategoria():
    """"
    body2= request.get_json()
    nit=body2['id']
    nombre=body2['nombre']
    descripcion=body2['descripcion']
    cargaTrabajo=body2['cargaTrabajo']"""

    lista2=request.data.decode('utf-8') 
    conver1=lista2.split(',')
    id1=str(conver1[0])
    nombre=str(conver1[1])
    descripcion=str(conver1[2])
    cargaTrabajo=str(conver1[3])
    
    with open('categoriaJson.json', "r") as file:
         data2 = json.load(file)
    data2['categoria'].append({'id':id1,'nombre': nombre,'descripcion': descripcion,'cargaTrabajo': cargaTrabajo})
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
    id2=body3['ID']
    id22=body3['id']
    nombre=body3['nombre']
    descripcion=body3['descripcion']
    idRC=body3['idR']
    cantidad=body3['Recursos']
    
    with open('cateconfigJson.json', "r") as file:
            data3 = json.load(file)
    data3['configuracion'].append({'ID':id2,'id':id22,'nombre': nombre,'descripcion': descripcion,'idR': idRC,'Recursos':cantidad})
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

    """
    body4= request.get_json()
    nit=body4['nit']
    nombre=body4['nombre']
    usuario=body4['usuario']
    direccion=body4['direccion']
    correoElectronico=body4['correoElectronico']"""
    lista4=request.data.decode('utf-8')
    conver4=lista4.split(',')
    nit=str(conver4[0])
    nombre=str(conver4[1])
    usuario=str(conver4[2])
    direccion=str(conver4[3])
    correoElectronico=str(conver4[4])
    
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
    """body5= request.get_json()
    id=body5['id']
    idConfiguracion=body5['idConfiguracion']
    nombre=body5['nombre']
    fechaInicio=body5['fechaInicio']
    estado=body5['estado']
    fechaFinal=body5['fechaFinal']"""
    lista5=request.data.decode('utf-8')
    conver5=lista5.split(',')
    id5=str(conver5[0])
    idConfiguracion=str(conver5[1])
    nombre=str(conver5[2])
    fechaInicio=str(conver5[3])
    estado=str(conver5[4])
    fechaFinal=str(conver5[5])

    with open ('instanciaJson.json', "r") as file:
        data5 = json.load(file)
    data5['instancia'].append({'id':id5,'idConfiguracion': idConfiguracion,'nombre': nombre,'fechaInicio': fechaInicio,'estado': estado,'fechaFinal': fechaFinal})
    with open('instanciaJson.json', "w") as file:
            json.dump(data5, file)
    Datos = {
                'message': 'Instancia agregada Exitosamente',
                'state':200
            }
    return jsonify(Datos)


@app.route('/crearFactura', methods=['POST'])
def crearFactura():
    
    "body= request.get_json()"
    lista6=request.data.decode('utf-8')
    conver6=lista6.split(',')
    nit=str(conver6[0])
   
    fechaInicio=str(conver6[1])
    fechaFinal=str(conver6[2])



    listita=[]
    listita2={}
    listita2['listaClientes']=[]

   
    
    listita3=[]
    listita31={}
    listita31['listaidre']=[]
    
    
    
    listita4=[]
    listita41={}
    listita41['listaRecursos']=[]

    listita51=[]
    listita5={}
    listita5['recursosprin']=[]

    """id=body['nitcliente']
    fechaInicio=body['fechaInicio']
    fechaFinal=body['fechaFinal']"""
   
    with open('consumoJson.json') as file:
       data = json.load(file)

    with open('clienteJSon.json', "r") as file:
        data2 = json.load(file)
    
    with open('instanciaJson.json', "r") as file:
        data3 = json.load(file)

    with open('cateconfigJson.json', "r") as file:
        data4 = json.load(file)

    with open('recursosJson.json', "r") as file:
        data5 = json.load(file)
 

    for consumo in data['consumo']:            
        if   nit==consumo['nitCliente']:                
            for cliente in data2['cliente']:
                if nit==cliente['nit']:
                    listita.append(cliente['nombre'])
                    listita.append(consumo['nitCliente'])
                    listita.append(consumo['idInstancia'])
                    listita.append(float(consumo['tiempo']))
                    listita.append(consumo['fechaHora'])
                    for instancia in data3['instancia']:
                        if consumo['idInstancia']==instancia['id']:
                            listita.append(instancia['idConfiguracion'])
                            for categoria in data4['configuracion']:
                                if instancia['idConfiguracion']==categoria['id']:
                                    listita.append(categoria['nombre'])
                                    listita.append(categoria['descripcion'])
                                    for recusos in categoria['idR']:                                        
                                        listita3.append(recusos)
                                    listita31['listaidre'].append(listita3)
                                    listita3=[]
                                    for recurso2 in categoria['Recursos']:
                                        listita4.append(recurso2)                                    
                                    #recursos de la categoria
                                    listita41['listaRecursos'].append(listita4)
                                    listita4=[]
                    """ factu.factur(listita2['listaClientes'],listita31['listaidre'],listita41['listaRecursos'],listita5['recursosprin'])
                    factu.factu2(listita2['listaClientes'],listita31['listaidre'],listita41['listaRecursos'],listita5['recursosprin'])"""
                    listita2['listaClientes'].append(listita)
                    listita=[]

#recursos oficial 0.02              
    for recurso in data5['recursos']:
        listita51.append(recurso['id'])
        listita51.append(recurso['nombre'])
        listita51.append(recurso['abreviatura'])
        listita51.append(recurso['metrica'])
        listita51.append(recurso['tipo'])
        listita51.append(recurso['valorXhora'])
        listita5['recursosprin'].append(listita51)
        listita51=[]
    factu.factur(listita2['listaClientes'],listita31['listaidre'],listita41['listaRecursos'],listita5['recursosprin'])
    factu.factu2(listita2['listaClientes'],listita31['listaidre'],listita41['listaRecursos'],listita5['recursosprin'])
    
    
    return jsonify(listita2,listita31,listita41,listita5)

""""@app.route('/ayuda', methods=['GET'])
def getcrearFactura():
    webbrowser.open_new_tab('[IPC2]Proyecto_3_2S2022-v2.pdf')
    dato={'msg':'Datos cargados'}  
    return jsonify(dato)"""
    
