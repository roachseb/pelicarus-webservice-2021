import urllib.request
UPDATEHELLOASSOTABLES = urllib.request.urlopen("http://127.0.0.1:8000/helloasso/actions").read()
print(UPDATEHELLOASSOTABLES)
updateMEMBERTABLE = urllib.request.urlopen("http://127.0.0.1:8000/filldb").read()
print(updateMEMBERTABLE)
updateMEMBERSDates = urllib.request.urlopen("http://127.0.0.1:8000/updatedb").read()
print(updateMEMBERSDates)
updateMailChimpList = urllib.request.urlopen("http://127.0.0.1:8000/updatemailchimp").read()
print(updateMailChimpList)