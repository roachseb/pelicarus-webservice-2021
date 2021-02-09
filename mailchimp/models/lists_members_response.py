

class LMResponse(object):
    def __init__(self,members,list_id,total_items,_links):
            self.members = [Members(**x) for x in members]
            self.list_id = list_id
            self.total_items = total_items
            self._links = _links

    def __str__(self):
        return self.__dict__.__str__()+'\n'

class Members(object):
    def __init__(self,id,email_address,unique_email_id,web_id,email_type,status,merge_fields,stats,ip_signup,
    timestamp_signup,ip_opt,timestamp_opt,member_rating,last_changed,language,vip,email_client,location,source,
    tags_count,tags,list_id,_links,unsubscribe_reason=None):
        self.id = id
        self.email_address = email_address
        self.unique_email_id = unique_email_id
        self.web_id = web_id
        self.email_type = email_type
        self.status = status
        self.merge_fields = Merge_fields(**merge_fields)

    def __str__(self):
        return self.__dict__.__str__()+'\n'

class Merge_fields(object):
    def __init__(self,FIRSTNAME,LASTNAME,ADDRESS,PHONE):
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.ADDRESS = ADDRESS
        self.PHONE = PHONE

    def __str__(self):
        return self.__dict__.__str__()+'\n'