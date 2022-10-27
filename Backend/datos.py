import xml.etree.ElementTree as ET
import re

from xml.dom import minidom as MD

class XML():
    
    def entrada(self,ruta):
          
        #file = open(ruta,'r', encoding="utf-8")
        # print(ruta)
        xmldoc = MD.parse(ruta) 
        ruta2= xmldoc.documentElement
        listandoR= ruta2.getElementsByTagName("listaRecursos")[0]
        recursos = listandoR.getElementsByTagName("recurso")
        for recurso in recursos:
            idR=recurso.getAttribute("id")
            nombreR=recurso.getElementsByTagName("nombre")[0].firstChild.data
            abrev=recurso.getElementsByTagName("abreviatura")[0].firstChild.data
            metric=recurso.getElementsByTagName("metrica")[0].firstChild.data
            valorXh=recurso.getElementsByTagName("valorXhora")[0].firstChild.data
            # aqui separar dato 

        listandoC= ruta2.getElementsByTagName("listaCategorias")[0]
        categoria=listandoC.getElementsByTagName("categoria")
        for cat in categoria:
            idC=cat.getAttribute("id")
            nombreC=cat.getElementsByTagName("nombre")[0].firstChild.data
            descrip=cat.getElementsByTagName("descripcion")[0].firstChild.data
            cargaTrab=cat.getElementsByTagName("cargaTrabajo")[0].firstChild.data
            configu=cat.getElementsByTagName("configuracion")
            #print(idC, nombreC, descrip, cargaTrab)
            # aqui separar dato 
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
                    #print(idRC,cantidadRecurC)
                    # aqui separar dato 
        
        listandoCl= ruta2.getElementsByTagName("listaClientes")[0]
        cliente=listandoCl.getElementsByTagName("cliente")
        for cli in cliente:
            idCl=cli.getAttribute("nit")
            nombreCl=cli.getElementsByTagName("nombre")[0].firstChild.data
            usuaCl=cli.getElementsByTagName("usuario")[0].firstChild.data
            direcCl=cli.getElementsByTagName("direccion")[0].firstChild.data
            correoCl=cli.getElementsByTagName("correoElectronico")[0].firstChild.data
            inst=cli.getElementsByTagName("instancia")
            #print(idCl, nombreCl, usuaCl, direcCl, correoCl)
            # aqui separar dato
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
                    
                

        
        
       
        




        
       