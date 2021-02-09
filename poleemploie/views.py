from django.shortcuts import render,redirect
from django.template import loader
from requests.auth import HTTPBasicAuth
import requests
import re
import pandas
import os.path



# Create your views here.
class PoleEmploie():
    def __init__(self):
        self.apikey = 'iqndwi1TKQ89dJQz212Ypf3PF4E'
        self.header = {'Authorization': 'Bearer ' + self.apikey}
    def getRequest(self,url) :
        return requests.get(url,verify=False)
    def postRequest(self,url,data) :
        return requests.post(url,data=data,headers={'Content-Type':	'application/x-www-form-urlencoded'})
 
    def to_csv(self,data):
        df = pandas.DataFrame.from_records(data)
        df.to_csv("output.csv",sep=';')

if __name__ == "__main__":
    pe = PoleEmploie()
    print(pe.apikey)

    links=[]
    out = []
    req = pe.getRequest('http://candidat.pole-emploi.fr/offres/recherche?lieux=978D&offresPartenaires=true&rayon=100&tri=0&range=0-100')
    for line in req.text.split():
        
        if 'href="/offres/recherche/detail/' in line:
            regex = r"\"(.+)\""
            links.append("https://candidat.pole-emploi.fr" + re.search(regex,line).group(1))

    print(links)
    for link in links:
        req = pe.getRequest(link)
        text = req.content.decode('UTF-8')
        title = re.search(r'<h1 itemprop="title" class="t2 title">(.+)</h1>',text).group(1)
        try:
            description = re.search(r'<div itemprop="description" (.+)><p>(.+)</p></div>',text).group(2)
        except:
            description = None

        out.append({'Title':title,'Description':description})
        pe.to_csv(out)
