
class AoUMRequest(object):
    def __init__(self,email_address,status_if_new,email_type,status,FIRSTNAME,LASTNAME,ADDRESS,PHONE):
        self.email_address = email_address
        self.status_if_new = status_if_new
        self.email_type = email_type
        self.status = status
        self.merge_fields = AoUMMerge_fields(FIRSTNAME,LASTNAME,ADDRESS,PHONE)

    def __str__(self):
        return self.__dict__.__str__()+'\n'

class AoUMMerge_fields(object):
    def __init__(self,FIRSTNAME,LASTNAME,ADDRESS,PHONE):
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.ADDRESS = ADDRESS
        self.PHONE = PHONE

    def __str__(self):
        return self.__dict__.__str__()+'\n'
