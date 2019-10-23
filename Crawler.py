import os
import requests
import PyPDF2
#from listaDeputados import lista_Deputados

#site de onde é pego essas informações
#https://www.al.ce.gov.br/index.php/transparencia/verba-de-desempenho-parlamentar



class Crawler:
    
    def __init__(self):
        pass

    def getUrl(self, nomeDeputado, mes, ano):
        urlBase = 'https://www.al.ce.gov.br/paineldecontrole/jumi_transparencia_deputados.php?act=vervdp'
        urlMes = '&f_mes=' + mes
        urlAno = '&f_ano=' + ano
        urlDep = '&f_dep=' + nomeDeputado.replace(' ','+')
        url = urlBase + urlAno + urlMes + urlDep
        return url
    
    def getNameFile(self, nomeDeputado, mes, ano):
        nameFile = nomeDeputado.replace(' ','') + ano + mes
        return nameFile

    def getPDF(self, url, nameFile):
        #url = self.getUrl(nomeDeputado, mes, ano)
        myFile = requests.get(url, allow_redirects=True)
        #nameFile = nomeDeputado.replace(' ') + ano + mes
        open('Files\\'+nameFile+'.pdf','wb').write(myFile.content)

    def execute(self, nomeDeputado, mes, ano, deleteFile = True):
        url = self.getUrl(nomeDeputado, mes, ano)
        nameFile = self.getNameFile(nomeDeputado, mes, ano)
        self.getPDF(url, nameFile)

