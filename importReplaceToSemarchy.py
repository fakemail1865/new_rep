import requests
from bs4 import BeautifulSoup # to read xml file


# Reading the data inside the xml
# file to a variable under the name
# data

name = "my_xml3"  # name of model you want to import
payload = ''
with open('{name}.xml'.format(name=name), 'r') as f:
    payload = payload + f.read()

headers = {
  'Content-Type': 'application/octet-stream',
  'Authorization': 'Basic c2VtYWRtaW46c2VtYWRtaW4=',
  'Cookie': 'XSRF-TOKEN=a3dc895f-3443-4952-8d6e-a492d2218e14'
}

#send post request to semarchy
name = "test"  # name of model you want to import
key = 0.0 
url = "http://localhost:8088/semarchy/api/rest/app-builder/models/{name}/editions/{key}/content".format(name=name,key=key)

response = requests.request("POST", url, headers=headers, data=payload)

print(response)
