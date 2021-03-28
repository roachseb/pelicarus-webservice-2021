import base64
import mimetypes
import os
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from os import listdir
from os.path import isfile, join

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Interface.RestAPI_Helper import GOOGLEAPI_HELPER


# Create your views here.
class GoogleMail(GOOGLEAPI_HELPER):
    def __init__(self):
        GOOGLEAPI_HELPER.__init__(self)
        self.userId = 'me'

    def create_message(self, sender, to, subject, message_text):
        """Create a message for an email.

        Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

        Returns:
        An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def create_message_html(self,sender, to, subject, html_file, attachement_folder=None):
        """Create a message for an email.

        Args:
            sender: Email address of the sender.
            to: Email address of the receiver.
            subject: The subject of the email message.
            html_message: The path to the html email template to be sent.
            attachement_folder: The path to the element to be sent as attachements

        Returns:
            An object containing a base64url encoded email object.
        """

        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        
        ## take html file turn into str to send
        try:
            with open(html_file, 'r') as f:
                html_string = f.read()
                message.attach(MIMEText(html_string,'html'))
                f.close()
        except Exception as e:
            print(e)

        ## for all of the file in the attachement folder 
        ### add file as attachement

        if attachement_folder is not None:
            onlyfiles = [f for f in listdir(attachement_folder) if isfile(join(attachement_folder, f))]

            for file in onlyfiles:
                content_type, encoding = mimetypes.guess_type(file)

                if content_type is None or encoding is not None:
                    content_type = 'application/octet-stream'
                main_type, sub_type = content_type.split('/', 1)
                if main_type == 'text':
                    fp = open(attachement_folder+"/"+file, 'r')
                    msg = MIMEText(fp.read(), _subtype=sub_type)
                    fp.close()
                elif main_type == 'image':
                    fp = open(attachement_folder+"/"+file, 'rb')
                    msg = MIMEImage(fp.read(), _subtype=sub_type)
                    fp.close()
                elif main_type == 'audio':
                    fp = open(attachement_folder+"/"+file, 'rb')
                    msg = MIMEAudio(fp.read(), _subtype=sub_type)
                    fp.close()
                else:
                    fp = open(attachement_folder+"/"+file, 'rb')
                    msg = MIMEBase(main_type, sub_type)
                    msg.set_payload(fp.read())
                    fp.close()

                filename = os.path.basename(file)
                msg.add_header('Content-Disposition', 'attachment', filename=filename)
                message.attach(msg)

        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def users_messages_send(self, userId='me', message=None):
        
        message = (self.service.users().messages().send(userId=userId, body=message).execute())
        print('Message Id: {}'.format(message['id']))
        return message
        


# view functions

def index(request):
    return HttpResponse("Welcome to Google Page {} ".format('hello'))




