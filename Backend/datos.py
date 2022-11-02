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

    global consumoJson
    

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

    consumoJson={}
    consumoJson['consumo']=[]

    contCli=0
    contInst=0
    contRe=0

    consum=0
    def entrada(self,ruta):
        
        #file = open(ruta,'r', encoding="utf-8")
        # print(ruta)
       
        listaI=[]
        listaR=[]
        file="C:\\Users\\ADMIIN\\Desktop\{}".format(ruta)
        
        xmldoc = MD.parse(file) 
        ruta2= xmldoc.documentElement
        listandoR= ruta2.getElementsByTagName("listaRecursos")[0]
        recursos = listandoR.getElementsByTagName("recurso")

#recursos---------------------------------------------------------------------
        contRe=0
        for recurso in recursos:
            contRe+=1
            idR=recurso.getAttribute("id")
            nombreR=recurso.getElementsByTagName("nombre")[0].firstChild.data
            abrev=recurso.getElementsByTagName("abreviatura")[0].firstChild.data
            metric=recurso.getElementsByTagName("metrica")[0].firstChild.data
            tipo=recurso.getElementsByTagName("tipo")[0].firstChild.data
            valorXh=recurso.getElementsByTagName("valorXhora")[0].firstChild.data
            # aqui separar dato 
            recursosJson['recursos'].append({'id':idR,'nombre': nombreR,'abreviatura': abrev,'metrica': metric,'tipo':tipo,'valorXhora': valorXh})
            self.contRe=contRe
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

                    
               
                    # aqui separar dato Backend 
                cateconfigJson['configuracion'].append({'ID':idC,'id':idConf,'nombre':nombreConf,'descripcion':descripcionConf,'idR': listaI,'Recursos': listaR})
                listaR=[]
                listaI=[]


#lista clientes-------------------------------------
        
        listandoCl= ruta2.getElementsByTagName("listaClientes")[0]
        cliente=listandoCl.getElementsByTagName("cliente")
        contCli=0
        contInst=0
        for cli in cliente:
            contCli+=1
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
            
                contInst+=1
                idInst=insta.getAttribute("id")
                idConf=insta.getElementsByTagName("idConfiguracion")[0].firstChild.data
                nombreInst=insta.getElementsByTagName("nombre")[0].firstChild.data
                fechaInst=insta.getElementsByTagName("fechaInicio")[0].firstChild.data
                #list=re.findall("\d{2}/\d{2}/\d{4}", fechaInst)
                lita=re.compile(r'([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})')
                obteni=lita.search(fechaInst)
                #print(obteni[0])
                estInst=insta.getElementsByTagName("estado")[0].firstChild.data
                if estInst == "Cancelada":
                    fechafinInst=insta.getElementsByTagName("fechaFinal")[0].firstChild.data
                    lita=re.compile(r'([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})')
                    obteni2=lita.search(fechafinInst)
                    fechafinInst=obteni2[0]
                else:
                    fechafinInst="---"
                          
                instanciaJson['instancia'].append({'id': idInst,'idConfiguracion': idConf,'nombre': nombreInst,'fechaInicio': obteni[0],'estado': estInst,'fechaFinal': fechafinInst})
                
        self.contCli=contCli
        self.contInst=contInst
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

    def getContCli(self):        
        return self.contCli

    def getContInst(self):
        return self.contInst

    def getContRe(self):
        return self.contRe
   


    def entrada2lectu(self, ruta2):
         
        file2="C:\\Users\\ADMIIN\\Desktop\{}".format(ruta2)        
        xmldoc = MD.parse(file2)  
        ruta3= xmldoc.documentElement
        consu = ruta3.getElementsByTagName("consumo")
        consum=0
        for cons in consu:
            nitConsu=cons.getAttribute("nitCliente")
            idInst=cons.getAttribute("idInstancia")
            tiempow=cons.getElementsByTagName("tiempo")[0].firstChild.data
            fechaConsu=cons.getElementsByTagName("fechaHora")[0].firstChild.data
            


            consumoJson['consumo'].append({'nitCliente': nitConsu,'idInstancia': idInst,'tiempo': tiempow,'fechaHora': fechaConsu})
            consum+=1
        
        self.consum=consum
        with open('consumoJson.json', 'w+') as file:
            json.dump(consumoJson, file, indent=4)


    def getConsum(self):
        return self.consum
            
                    
                

        
        
       
        




        
       