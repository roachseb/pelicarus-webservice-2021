import json
import os
from datetime import date, datetime,timedelta

import requests
from dateutil.relativedelta import relativedelta
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from requests.auth import HTTPBasicAuth
from django.db.models import Q

from mailchimp.views import MailChimp

from google.views import GoogleMail

from helloasso.models import Action, Campaign, CustomInfo, Organism, Payment

from .models import Member,Event
from mailchimp.models.add_or_update_member_request import AoUMRequest

from pandas import DataFrame


class MyApp():
    def __init__(self):
        self.comite_directeur = ['comitedirecteur@pelicarus.org']
        self.Member_info_chain = ['comitedirecteur@pelicarus.org','administration@pelicarus.org','pole.communication@pelicarus.org','pole.parrainage@pelicarus.org','pole.relationpro@pelicarus.org']




# Create your views here.
def index(request):
    tmpt = loader.get_template("./home/index.html")
    context = {
        'ex': 0
    }
    return HttpResponse(tmpt.render(context, request))


def filldatabase(request):
    actionquery = Action.objects.filter(type="SUBSCRIPTION").filter(Q(campaign=1081473)|Q(campaign=221403))

    for e in actionquery:
        print(str(e.campaign).encode(encoding='UTF-8',errors='strict') )
        # setting end date
        new_date = e.date + relativedelta(years=1)
        if date.today() < new_date:
            b = True
        else:
            b = False

        m = Member(
            firstname=e.first_name,
            lastname=e.last_name,
            email=e.email,
            subscription_date=e.date,
            end_subscription_date=new_date,
            active=b
        )

        try:
            m.save()
        except IntegrityError:
            # manage update
            dbmem = Member.objects.get(firstname=m.firstname,lastname=m.lastname,email=m.email)
            if m.subscription_date > dbmem.subscription_date:
                dbmem.delete()
                m.save()
                print('Updated : {}'.format(m).encode(encoding='UTF-8',errors='strict') )
            else:
                print('Duplicate : {}'.format(m).encode(encoding='UTF-8',errors='strict') )

    campaignquery = Campaign.objects.filter(type="EVENT")

    for e in campaignquery:
        event = Event(
            name=e.name,
            url=e.url,
            creation_date=e.creation_date,
            place_name=e.place_name,
            place_address=e.place_address,
            place_city=e.place_city,
            place_zipcode=e.place_zipcode,
            place_country=e.place_country
        )
        try:
            event.save()
        except IntegrityError:
                print('Duplicate -- event : {}'.format(event).encode(encoding='UTF-8',errors='strict') )
            #event.save(update_fields=['creation_date','place_name','place_address','place_city','place_zipcode','place_country'])    

    return HttpResponse("soon")

def updatememberdate(request):
    ''' Evaluate the validation of a members subscribetion
        sends a mail if they are marked as not subscribed 
    '''
    allmembers = Member.objects.all()
    output=[]

    # date checking 
    for member in allmembers:

        if date.today() > member.end_subscription_date and (member.active == True):
            output.append('updating : %s <br>'%(member))
            member.active = False
            member.save()
            # Send a gmail to annonce their expired subscription
            gm = GoogleMail()
            message = gm.create_message_html('administration@pelicarus.org',str(member.email),'[ignore demo]Expired Pelicarus Membership','C:/Users/Productivity/Desktop/PelicarusWS/google/templates/emails/unsubscribed_notification/index.htm')
            gm.users_messages_send(message=message)

        else:
            output.append('no change : %s <br>'%(member))
        
    return HttpResponse(output)

def updatemailchimp(request):
    mc = MailChimp()
    memberquery = Member.objects.all()
    output = []

    for member in memberquery:
        if member.active:
            output.append(member)
            mc.Add_or_update_list_member(mc.adlist,AoUMRequest(member.email,'subscribed','html','subscribed',member.firstname,member.lastname,'',member.phonenumber))
        else:
            mc.Add_or_update_list_member(mc.adlist,AoUMRequest(member.email,'unsubscribed','html','unsubscribed',member.firstname,member.lastname,'',member.phonenumber))

    return HttpResponse(output)

def send_active_member_info(request):

    # Setup date variables
    today_date = date.today()
    next_month = today_date + timedelta(weeks=4)
    previous_month = today_date - timedelta(weeks=4)

    # get all the current members info
    CurrentActiveMembers = Member.objects.filter(active=True)
    LastMonthExpiredMembers = Member.objects.filter(end_subscription_date__range=[previous_month,today_date])

    # format that into csv [french and english]
    ## Developer Comments : Might be better to use drive as a method to send csv data
    CAM = []
    for m in CurrentActiveMembers:
        CAM.append([m.firstname,m.lastname,m.email,m.subscription_date,m.end_subscription_date,m.active,(m.end_subscription_date <= next_month)])
    LMEM = []
    for m in LastMonthExpiredMembers:
        LMEM.append([m.firstname,m.lastname,m.email,m.subscription_date,m.end_subscription_date,m.active,False])
    CAM = CAM+LMEM

    # Create Dataframe
    df_info = DataFrame(CAM,columns=["Firstname","Lastname","Email","Subscription Date","Expiration Date","Active","Expired In A Month"])
    # Dataframe to Csv
    df_info.to_csv("/tmp/member_info_english.csv")
    df_info.to_csv("/tmp/member_info_french.csv",sep=';')

    # send mail to all pole of the association
    gm = GoogleMail()
    for email in MyApp().Member_info_chain:
        gm_msg = gm.create_message_html("administration@pelicarus.org",email,"[ignore demo]Current Members Info","","/tmp/")
        gm.users_messages_send(message=gm_msg)


    # remove csv local files
    if os.path.exists("/tmp/member_info_english.csv"):
        os.remove("/tmp/member_info_english.csv")
    if os.path.exists("/tmp/member_info_french.csv"):
        os.remove("/tmp/member_info_french.csv")

    return HttpResponse("Mail Sent")




def handler404(request,exception):
    return render(request, './home/404.html', status=404)

def handler500(request):
    return render(request, './home/404.html', status=500)