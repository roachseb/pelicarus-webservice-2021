import requests,json
import hashlib 

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Interface.RestAPI_Helper import RESTAPI_HELPER
from myapp.models import Member
from requests.auth import HTTPBasicAuth

from .models.lists_members_response import LMResponse,Members
from .models.add_or_update_member_request import AoUMRequest,AoUMMerge_fields

# Create your views here.

class MailChimp(RESTAPI_HELPER):

    def __init__(self):
        RESTAPI_HELPER.__init__(self)
        
        self._baseURL = self._Configuration.mailchimp['api_base_url']
        self.apikey=self._Configuration.mailchimp['api_key']
        self.user=self._Configuration.mailchimp['user']
        self.adlist=self._Configuration.mailchimp['official_list']
        self.testadlist=self._Configuration.mailchimp['tester_list']

    #### Private Methods 

    def __get(self,url):
        print(self.user)
        return self._session.get(url, auth=HTTPBasicAuth(self.user,self.apikey))

    def __post(self,url,json=None):
        return self._session.post(url, auth=HTTPBasicAuth(self.user,self.apikey),data=json)

    def __put(self,url,json=None):
        return self._session.put(url, auth=HTTPBasicAuth(self.user,self.apikey),data=json)

    def __delete(self,url):
        return self._session.delete(url,auth=HTTPBasicAuth(self.user,self.apikey))


    #### Work Methods

    def List_members_info(self,listid):
        '''Returns the json body response of the list/member info of mailchimp
        '''
        r = self.__get('https://us11.api.mailchimp.com/3.0/lists/{}/members'.format(listid))
        try:
            return LMResponse(**r.json())
        except:
            return r


    def Add_or_update_list_member(self, listid,JsonObject:AoUMRequest):
        '''
            JSON EXAMPLE:
        {
            "email_address": "urist.mcvankab@freddiesjokes.com",
            "status": "subscribed",
            "merge_fields": {
                "FIRSTNAME": "Urist",
                "LASTNAME": "McVankab"
            }
        }
        '''
        subscriber_hash = hashlib.md5(JsonObject.email_address.encode()).hexdigest()

        r= self.__put("https://us11.api.mailchimp.com/3.0/lists/{}/members/{}".format(listid,subscriber_hash),json.dumps(JsonObject,default=lambda x: x.__dict__))
        try:
            return Members(**r.json())
        except:
            return r


    def deleteMemberfromList(self,listid,JsonObject:AoUMRequest):

        subscriber_hash = hashlib.md5(JsonObject.email_address.encode()).hexdigest()

        r= self.__post("https://us11.api.mailchimp.com/3.0//lists/{}/members/{}/actions/delete-permanent".format(listid,subscriber_hash),None)
        try:
            return Members(**r.json())
        except:
            return r
    

#### view functions

def index(request):
    return HttpResponse("Mailchimp Mail Page")

def updatemailchimplist(request):
    pass


def listinfo(request):
    mc = MailChimp()
    return HttpResponse(mc.List_members_info(mc.adlist).members)



