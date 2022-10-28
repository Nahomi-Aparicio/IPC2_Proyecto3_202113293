from xml.dom.minidom import *
import re
from datetime import datetime
import json
from xml.dom import minidom as MD

class XML():
    global recursosJson
    global categoriaJson
    global cateconfigJson
    global  clienteJSon
    global  instanciaJson

    recursosJson={}
    recursosJson['recursos']=[]

    categoriaJson={}
    categoriaJson['categoria']=[]

    cateconfigJson={}
    cateconfigJson['configuracion']=[]

    clienteJSon={}
    clienteJSon['cliente']=[]

    instanciaJson={}
    instanciaJson['instancia']=[]
   

    def entrada(self,ruta):
          
        #file = open(ruta,'r', encoding="utf-8")
        # print(ruta)
       
        listaI=[]
        listaR=[]
        xmldoc = MD.parse(ruta) 
        ruta2= xmldoc.documentElement
        listandoR= ruta2.getElementsByTagName("listaRecursos")[0]
        recursos = listandoR.getElementsByTagName("recurso")

#recursos---------------------------------------------------------------------

        for recurso in recursos:
            idR=recurso.getAttribute("id")
            nombreR=recurso.getElementsByTagName("nombre")[0].firstChild.data
            abrev=recurso.getElementsByTagName("abreviatura")[0].firstChild.data
            metric=recurso.getElementsByTagName("metrica")[0].firstChild.data
            tipo=recurso.getElementsByTagName("tipo")[0].firstChild.data
            valorXh=recurso.getElementsByTagName("valorXhora")[0].firstChild.data
            # aqui separar dato 
            recursosJson['recursos'].append({'id':idR,'nombre': nombreR,'abreviatura': abrev,'metrica': metric,'tipo':tipo,'valorXhora': valorXh})
# categorias ------------------------------------------------------------
        listandoC= ruta2.getElementsByTagName("listaCategorias")[0]
        categoria=listandoC.getElementsByTagName("categoria")
        for cat in categoria:
            idC=cat.getAttribute("id")
            nombreC=cat.getElementsByTagName("nombre")[0].firstChild.data
            descrip=cat.getElementsByTagName("descripcion")[0].firstChild.data
            cargaTrab=cat.getElementsByTagName("cargaTrabajo")[0].firstChild.data
            configu=cat.getElementsByTagName("configuracion")
            #print(idC, nombreC, descrip, cargaTrab)
            categoriaJson['categoria'].append({'id':idC,'nombre': nombreC,'descripcion': descrip,'cargaTrabajo': cargaTrab})
# configuracion------------------------------------------------------------ 
            for confi in configu:
                idConf=confi.getAttribute("id")
                nombreConf=confi.getElementsByTagName("nombre")[0].firstChild.data
                descripcionConf=confi.getElementsByTagName("descripcion")[0].firstChild.data
                recurConfig=confi.getElementsByTagName("recurso")
                #print(idConf, nombreConf, descripcionConf)
                # aqui separar dato

                for recurC in recurConfig:
                    idRC=recurC.getAttribute("id")
                    cantidadRecurC=recurC.firstChild.data
                    listaI.append(idRC)
                    listaR.append(cantidadRecurC)

                    
                print(listaI)
                print(listaR)
                    # aqui separar dato Backend 
                cateconfigJson['configuracion'].append({'ID':idC,'id':idConf,'nombre':nombreConf,'descripcion':descripcionConf,'idR': listaI,'Recursos': listaR})
                listaR=[]
                listaI=[]


#lista clientes-------------------------------------
        listandoCl= ruta2.getElementsByTagName("listaClientes")[0]
        cliente=listandoCl.getElementsByTagName("cliente")
        for cli in cliente:
            idCl=cli.getAttribute("nit")
            nombreCl=cli.getElementsByTagName("nombre")[0].firstChild.data
            usuaCl=cli.getElementsByTagName("usuario")[0].firstChild.data
            direcCl=cli.getElementsByTagName("direccion")[0].firstChild.data
            correoCl=cli.getElementsByTagName("correoElectronico")[0].firstChild.data
            inst=cli.getElementsByTagName("instancia")
            #print(idCl, nombreCl, usuaCl, direcCl, correoCl)  instanciaJson
            clienteJSon['cliente'].append({'nit':idCl,'nombre': nombreCl,'usuario': usuaCl,'direccion': direcCl,'correoElectronico': correoCl})
            
#instancua datos----------------------------------------------------------
            for insta in inst:
            
                idInst=insta.getAttribute("id")
                idConf=insta.getElementsByTagName("idConfiguracion")[0].firstChild.data
                nombreInst=insta.getElementsByTagName("nombre")[0].firstChild.data
                fechaInst=insta.getElementsByTagName("fechaInicio")[0].firstChild.data
                estInst=insta.getElementsByTagName("estado")[0].firstChild.data
                if estInst == "Cancelada":
                    fechafinInst=insta.getElementsByTagName("fechaFinal")[0].firstChild.data
                else:
                    fechafinInst="---"                
                instanciaJson['instancia'].append({'id': idInst,'idConfiguracion': idConf,'nombre': nombreInst,'fechaInicio': fechaInst,'estado': estInst,'fechaFinal': fechafinInst})

        with open('recursosJson.json', 'w+') as file:
            json.dump(recursosJson, file, indent=4)

        with open('categoriaJson.json', 'w+') as file:
            json.dump(categoriaJson, file, indent=4)
        
        with open('cateconfigJson.json', 'w+') as file:
            json.dump(cateconfigJson, file, indent=4)

        with open('instanciaJson.json', 'w+') as file:
            json.dump(instanciaJson, file, indent=4)

        with open('clienteJSon.json', 'w+') as file:
            json.dump(clienteJSon, file, indent=4)





    def entrada2lectu(self, ruta2):
        xmldoc = MD.parse(ruta2) 
        ruta3= xmldoc.documentElement
        consu = ruta3.getElementsByTagName("consumo")
        for cons in consu:
            nitConsu=cons.getAttribute("nitCliente")
            idInst=cons.getAttribute("idInstancia")
            tiempow=cons.getElementsByTagName("tiempo")[0].firstChild.data
            fechaConsu=cons.getElementsByTagName("fechaHora")[0].firstChild.data
           
            print(nitConsu, idInst, tiempow, fechaConsu)
                    
                

        
        
       
        




        
       