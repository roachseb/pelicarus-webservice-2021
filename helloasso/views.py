import json
import os
from datetime import datetime

import requests
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.template import loader
from requests.auth import HTTPBasicAuth
from .Mmodels.actions_response import Action_Response
from .Mmodels.organisms_response import Organism_Response
from .Mmodels.campaign_response import Campaign_Response
from helloasso.models import Action, Campaign, CustomInfo, Organism, Payment

from .models import Action
from Interface.RestAPI_Helper import RESTAPI_HELPER


class HelloAsso(RESTAPI_HELPER):
    def __init__(self):
        RESTAPI_HELPER.__init__(self)
        self._baseURL = self._Configuration.helloasso['api_base_url']
        self.apikey = self._Configuration.helloasso['api_key']
        self.user = self._Configuration.helloasso['user']
        print(self.user,self.apikey)

    ## Private Methods
    def __get(self, url):
        return self._session.get(url, auth=HTTPBasicAuth(self.user, self.apikey))

    ## Public Methods
    def getActions(self):
        r = self.__get(
            self._baseURL+'actions.json?page=1&results_per_page=1000').json()

        responseData = Action_Response(**r)

        for resource in responseData.resources:
            
            last_name = resource.last_name
            first_name = resource.first_name
            payment = resource.id_payment
            id = int(resource.id)
            campaign = resource.id_campaign
            organism = resource.id_organism
            date = datetime.strptime(str(resource.date)[:-1], "%Y-%m-%dT%H:%M:%S.%f")
            amount = resource.amount
            type = resource.type
            email = resource.email
            status = resource.status
            option_label=resource.option_label

            o = Organism.objects.get(pk=int(organism))

            try:
                c = Campaign.objects.get(pk=int(campaign))
            except:
                c = None
                print('Could not find Campaign:{} to associate Action:{}\n'.format(c,id))

            action = Action(id=id,
                            first_name=first_name, last_name=last_name, email=email, type=type, date=date,
                            amount=amount, status=status, organism=o, campaign=c)
            try:
                action.save()
            except:
                print('Issue saving in Database, Action:{} \n'.format(action))
            # print(id,campaign,organism,payment,first_name,last_name,amount,date,email,type)
            # sub query Custom Info

            try:
                for el in resource.custom_infos:
                    cu = CustomInfo(label=el.label,value=el.value, action=action)
                    cu.save()
            except:
                print('Issue saving in Database, Custom_info{} \n'.format(cu))

    def getActionsDonation(self):
        r = self.__get(
            self._baseURL+'https://api.helloasso.com/v3/actions.json?type=DONATION&page=1&results_per_page=1000').json()

        for e in r['resources']:
            try:
                last_name = e['last_name']
            except KeyError:
                last_name = None

            try:
                first_name = e['first_name']
            except KeyError:
                first_name = None

            try:
                payment = e['id_payment']
            except KeyError:
                payment = None

            id = int(e['id'])
            campaign = e['id_campaign']
            organism = e['id_organism']
            date = datetime.strptime(
                str(e['date'])[:-1], "%Y-%m-%dT%H:%M:%S.%f")
            amount = e['amount']
            type = e['type']
            email = e['email']
            status = e['status']
            # option_label=e['option_label']

            o = Organism.objects.get(pk=int(organism))

            try:
                c = Campaign.objects.get(pk=int(campaign))
            except:
                c = None
                print('Issue with %s' % (c))
            action = Action(id=id,
                            first_name=first_name, last_name=last_name, email=email, type=type, date=date,
                            amount=amount, status=status, organism=o, campaign=c)
            action.save()
            # print(id,campaign,organism,payment,first_name,last_name,amount,date,email,type)
            # sub query Custom Info
            try:
                for el in e['custom_infos']:
                    cu = CustomInfo(label=el['label'],
                                    value=el['value'], action=action)
                    cu.save()
            except:
                print('Issue with %s' % (cu))

    def getActionsSubscription(self):
        r = self.__get(
            self._baseURL+'actions.json?type=SUBSCRIPTION&page=1&results_per_page=1000').json()

        for e in r['resources']:
            try:
                last_name = e['last_name']
            except KeyError:
                last_name = None

            try:
                first_name = e['first_name']
            except KeyError:
                first_name = None

            try:
                payment = e['id_payment']
            except KeyError:
                payment = None

            id = int(e['id'])
            campaign = e['id_campaign']
            organism = e['id_organism']
            date = datetime.strptime(
                str(e['date'])[:-1], "%Y-%m-%dT%H:%M:%S.%f")
            amount = e['amount']
            type = e['type']
            email = e['email']
            status = e['status']
            # option_label=e['option_label']

            o = Organism.objects.get(pk=int(organism))

            try:
                c = Campaign.objects.get(pk=int(campaign))
            except:
                c = None
                print('Issue with %s' % (c))

            action = Action(id=id,
                            first_name=first_name, last_name=last_name, email=email, type=type, date=date,
                            amount=amount, status=status, organism=o, campaign=c)
            action.save()
            # print(id,campaign,organism,payment,first_name,last_name,amount,date,email,type)
            # sub query Custom Info

            try:
                for el in e['custom_infos']:
                    cu = CustomInfo(label=el['label'],
                                    value=el['value'], action=action)
                    cu.save()
            except:
                print('Issue with %s' % (cu))

    def getActionsInscription(self):
        r = self.__get(
            self._baseURL+'actions.json?type=INSCRIPTION&page=1&results_per_page=1000').json()

        for e in r['resources']:
            try:
                last_name = e['last_name']
            except KeyError:
                last_name = None

            try:
                first_name = e['first_name']
            except KeyError:
                first_name = None

            try:
                payment = e['id_payment']
            except KeyError:
                payment = None

            id = int(e['id'])
            campaign = e['id_campaign']
            organism = e['id_organism']
            date = datetime.strptime(
                str(e['date'])[:-1], "%Y-%m-%dT%H:%M:%S.%f")
            amount = e['amount']
            type = e['type']
            email = e['email']
            status = e['status']
            # option_label=e['option_label']

            o = Organism.objects.get(pk=int(organism))

            try:
                c = Campaign.objects.get(pk=int(campaign))
            except:
                c = None
                print('Issue with %s' % (c))

            action = Action(id=id,
                            first_name=first_name, last_name=last_name, email=email, type=type, date=date,
                            amount=amount, status=status, organism=o, campaign=c)
            action.save()
            # print(id,campaign,organism,payment,first_name,last_name,amount,date,email,type)
            # sub query Custom Info

            try:
                for el in e['custom_infos']:
                    cu = CustomInfo(label=el['label'],
                                    value=el['value'], action=action)
                    cu.save()
            except:
                print('Issue with %s' % (cu))

    def getOrganisms(self):
        r =self.__get(self._baseURL+'organizations.json?page=1&results_per_page=1000').json()
        responseData = Organism_Response(**r)

        for resource in responseData.resources:
            o = Organism(
                resource.id,
                resource.name,
                resource.slug,
                resource.type,
                resource.funding,
                resource.supporters,
                resource.logo,
                resource.thumbnail,
                resource.profile,
                resource.donate_form
            )

            try:
                o.save()
            except:
                print('Issue saving in Database, Organism:{} \n'.format(o))


    def getCampaign(self):
        r = self.__get(self._baseURL+'campaigns.json?page=1&results_per_page=1000').json()
        responseData = Campaign_Response(**r)

        ## Manage the Json incoming data
        for resource in responseData.resources:
            name = resource.name
            slug = resource.slug
            type = resource.type
            state = resource.state
            id = resource.id
            funding = resource.funding
            supporters = resource.supporters
            url = resource.url
            organism = resource.id_organism
            slug_organism = resource.slug_organism
            creation_date = datetime.strptime(str(resource.creation_date)[:-1], "%Y-%m-%dT%H:%M:%S.%f")
            last_update = str(resource.last_update)
            place_name = resource.place_name
            place_address = resource.place_address
            place_city = resource.place_city
            place_zipcode = resource.place_zipcode
            place_country = resource.place_country
            start_date = datetime.strptime(str(resource.start_date), "%Y-%m-%dT%H:%M:%S") if resource.start_date is not None else None
            end_date = datetime.strptime(str(resource.end_date)[:-1], "%Y-%m-%dT%H:%M:%S") if resource.end_date is not None else None


            if organism is not None:
                o = Organism.objects.get(pk=int(organism))
            else:
                o = Organism.objects.get(pk=int(1009561))
            c = Campaign(id=id, name=name, slug=slug, type=type, state=state,
                         funding=funding, supporters=supporters, url=url, organism=o, slug_organism=slug_organism,
                         creation_date=creation_date, last_update=last_update, place_name=place_name,
                         place_address=place_address, place_city=place_city, place_zipcode=place_zipcode, place_country=place_country,
                         start_date=start_date, end_date=end_date)
            
            ## Save to the database

            try:
                c.save() 
            except IntegrityError:
                c.save(update_fields=['type','creation_date',
                'place_name','place_address','place_city','place_zipcode','start_date','end_date','state'])

        
    def getPayments(self):
        r = self.__get(self._baseURL+'payments.json?page=1&results_per_page=1000')


# Create your views here.

def index(request):

    template = loader.get_template('base/index.html')
    context = {
        'ex': 0
    }
    return HttpResponse(template.render(context, request))


def actions(request):
    ha = HelloAsso()
    ha.getActions()
    ha.getActionsSubscription()
    ha.getActionsInscription()
    #ha.getActionsDonation()
    return HttpResponse("Updated the Action Table")


def actions_subscribed(request):
    subscribedact = Action.objects.filter(type="SUBSCRIPTION")
    res = []
    for e in subscribedact:
        res.append(e)
    return HttpResponse(str(res))


def organisms(request):
    ha = HelloAsso()
    ha.getOrganisms()
    return HttpResponse("Updated the Organisme Table")


def payments(request):
    ha = HelloAsso()
    ha.getPayments()
    return HttpResponse("Updated the Payments Table : Method not implemented")


def campaigns(request):
    ha = HelloAsso()
    ha.getCampaign()
    return redirect('helloasso')
