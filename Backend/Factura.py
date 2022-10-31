import json
import re
import webbrowser

class haciendoFact:
 
    def factur(self,client,idre,re,recur):
        listita=[]
        htmlsalida = open("salida.html", "w", encoding="utf-8")
        html="<!DOCTYPE html>\n"
        html+="<html>\n"
        html+="<head>\n"
        html+="</head>\n"
        html+="<body>\n"
        for i in range(len(client)):
            html+='-------------------------------------'
            html+="<h1>Factura N° "+str(i+1)+"</h1>\n"
            html+="<p>Cliente: "
            html+=client[i][0]
            html+="</p>\n"
            r=0
            for j in range(len(idre[i])):
                html+="<p>Id: "+idre[i][j]+"</p>\n"
                
                for y in range(len(recur)):
                    if recur[y][0]==idre[i][j]:
                        for k in range(len(re[i])):
                            html+="<p>Recurso: "+re[i][k]+"</p>\n"
                            tot=float(client[i][3])*float(recur[y][5])*float(re[i][k+r])
                            html+="<p>Total del recurso: "+str(tot)+"</p>\n"
                            r+=1
                            listita.append(tot)
                            break
            totalFac=0
            print(listita)
            for li in range(len(listita)):
                totalFac+=float(listita[li])
            html+="<h3>Total de la factura: "+str(totalFac)+"</h3>\n"
            html+='-------------------------------------'
            listita=[]
                     
        html+="</body>\n"
        html+="</html>\n"
        htmlsalida.write(html)
        htmlsalida.close()
        webbrowser.open_new_tab('salida.html')

                        
    def factu2(self,client,idre,re,recur):
        listita=[]
        print(client)
        print(idre)
        print(re)
        print(recur)
        htmlsalida = open("salida2.html", "w", encoding="utf-8")
        html="<!DOCTYPE html>\n"
        html+="<html>\n"
        html+="<head>\n"
        html+="</head>\n"
        html+="<body>\n"
        for i in range(len(client)):
           
            html+='-------------------------------------'
            html+="<h1>Factura N° "+str(i+1)+"</h1>\n"
            html+="<p>Cliente: "+client[i][0]+"</p>\n"
            html+="<p>Nit del cliente: "+client[i][1]+"</p>\n"
            html+="<p>ID de instancia"+client[i][2]+"</p>\n"
            html+="<p>Horas de uso: "+str(client[i][3])+"</p>\n"
            html+="<p>-------------------------------------</p>\n"
            r=0
            for j in range(len(idre[i])):
                
                html+="<p>ID de recurso: "+idre[i][j]+"</p>\n"
                for y in range(len(recur)):
                    if recur[y][0]==idre[i][j]:
                        html+="<p>tiempo de consumo: "+str(float(client[i][3])*float(recur[y][5]))+"</p>\n"
                        for k in range(len(re[i])):
                            html+="<p>cantidad de recurso usado : "+re[i][k+r]+"</p>\n"
                            html+="<p>nombre del recurso: "+recur[y][1]+"</p>\n"
                            html+="<p> abreviatura : "+recur[y][2]+"</p>\n"
                            html+="<p> metrica del recurso: "+recur[y][3]+"</p>\n"
                            html+="<p> tipo de recurso: "+recur[y][4]+"</p>\n"
                            html+="<p> precio del recurso: "+recur[y][5]+"</p>\n"
                            tot=float(client[i][3])*float(recur[y][5])*float(re[i][k+r])
                            html+="<p>Total del recurso: "+str(tot)+"</p>\n"
                            html+="<p>-------------------------------------</p>\n"
                            r+=1
                            listita.append(tot)
                            break
            totalFac=0
            for li in range(len(listita)):
                totalFac+=float(listita[li])
            html+="<h3>Total de la factura: "+str(totalFac)+"</h3>\n"
            html+='-------------------------------------'
            listita=[]
                     
        html+="</body>\n"
        html+="</html>\n"
        htmlsalida.write(html)
        htmlsalida.close()
        webbrowser.open_new_tab('salida2.html')
                  
        