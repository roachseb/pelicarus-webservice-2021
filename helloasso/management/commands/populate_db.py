from django.core.management.base import BaseCommand
from helloasso.models import Action,Campaign,CustomInfo,Payment,Organism
import requests,os, json
from datetime import datetime
from dateutil.parser import parse
from requests.auth import HTTPBasicAuth

class HelloAsso:
    def __init__(self):
        with open(os.path.dirname(os.path.abspath(__file__))+'/credentials.json', 'r') as f:
            self.credentials = json.load(f)
        self.apikey=self.credentials['Apikey']
        self.user=self.credentials['User']

    def getRequest(self,url):
        return requests.get(url, auth=HTTPBasicAuth(self.user,self.apikey),)

    def getActions(self):
        r = self.getRequest('https://api.helloasso.com/v3/actions.json?page=1&results_per_page=1000').json()
        
        for e in r['resources']:
            try:
                last_name=e['last_name']
            except KeyError:
                last_name=None

            try:
                first_name=e['first_name']
            except KeyError:
                first_name=None

            try:
                payment=e['id_payment']
            except KeyError:
                payment=None


            id = int(e['id'])
            campaign = e['id_campaign']
            organism = e['id_organism']
            date = datetime.strptime(str(e['date'])[:-1], "%Y-%m-%dT%H:%M:%S.%f")
            amount = e['amount']
            type = e['type']
            email = e['email']
            status=e['status']
            #option_label=e['option_label']
            
            o = Organism.objects.get(pk=int(organism))

            c = Campaign.objects.get(pk=int(campaign))
            action=Action(id=id,
            first_name=first_name,last_name=last_name,email=email,type=type,date=date,
            amount=amount,status=status,organism=o, campaign=c)
            action.save()
            #print(id,campaign,organism,payment,first_name,last_name,amount,date,email,type)
            #sub query Custom Info
            try:
                for el in e['custom_infos']:
                    cu = CustomInfo(label=el['label'],value=el['value'],action=action)
                    cu.save()
            except KeyError:
                print([])
            
    def getOrganisms(self):
        r = self.getRequest('https://api.helloasso.com/v3/organizations.json?page=1&results_per_page=1000').json()

        for e in r['resources']:
            try:
                name=e['name']
            except KeyError:
                name=None
            try:
                slug=e['slug']
            except KeyError:
                slug=None
            try:
                type=e['type']
            except KeyError:
                type=None

            try:
                donate_form=e['donate_form']
            except KeyError:
                donate_form=None


            id = e['id']
            funding = e['funding']
            supporters = e['supporters']
            logo = e['logo']
            thumbnail = e['thumbnail']
            profile = e['profile']=type
            Organism(id=id,funding=funding,supporters=supporters,logo=logo,
            thumbnail=thumbnail,profile=profile,name=name,slug=slug,
            type=type,donate_form=donate_form).save()

    def getCampaign(self):
        r = self.getRequest('https://api.helloasso.com/v3/campaigns.json?page=1&results_per_page=1000').json()
        
        for e in r['resources']:
            try:
                name=e['name']
            except KeyError:
                name=None
            try:
                slug=e['slug']
            except KeyError:
                slug=None
            try:
                type=e['type']
            except KeyError:
                type=None
            try:
                state=e['state']
            except KeyError:
                state=None
            
            id = e['id']
            funding = e['funding']
            supporters = e['supporters']
            try:
                url = e['url']
            except KeyError:
                url=None

            try:
                organism = e['id_organism']
            except KeyError:
                organism=None

            try:
                slug_organism = e['slug_organism']
            except KeyError:
                slug_organism = None
            creation_date = datetime.strptime(str(e['creation_date'])[:-1], "%Y-%m-%dT%H:%M:%S.%f")
            last_update = str(e['last_update'])
            try:
                place_name = e['place_name']
            except KeyError:
                place_name = None
            try:
                place_address = e['place_address']
            except KeyError:
                place_address = None
            try:
                place_city = e['place_city']
            except KeyError:
                place_city = None
            try:
                place_zipcode = e['place_zipcode']
            except KeyError:
                place_zipcode = None
            try:
                place_country = e['place_country']
            except KeyError:
                place_country = None
            try:
                start_date = datetime.strptime(str(e['start_date']), "%Y-%m-%dT%H:%M:%S")
            except KeyError:
                start_date = None
            try:
                end_date = datetime.strptime(str(e['end_date'])[:-1], "%Y-%m-%dT%H:%M:%S")
            except KeyError:
                end_date = None

            if organism is not None:
                o = Organism.objects.get(pk=int(organism))
            else: 
                o = None
            Campaign(id=id,name=name,slug=slug,type=type,state=state,
            funding=funding,supporters=supporters,url=url,organism=o,slug_organism=slug_organism,
            creation_date=creation_date,last_update=last_update,place_name=place_name,
            place_address=place_address,place_city=place_city,place_zipcode=place_zipcode,place_country=place_country,
            start_date=start_date,end_date=end_date).save()
    
    def getPayments(self):
        r = self.getRequest('https://api.helloasso.com/v3/payments.json?page=1&results_per_page=1000')


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        ha = HelloAsso()
        ha.getOrganisms()
        ha.getCampaign()
        ha.getActions()
        
    def handle(self, *args, **options):
        self._create_tags()