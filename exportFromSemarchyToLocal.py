import requests
from requests.auth import HTTPBasicAuth

name = "KingsCrownBOA"  # name of model you want to import
key = 0.0   # version of the model

#url the request is sent to
url = 'http://localhost:8088/semarchy/api/rest/app-builder/models/{name}/editions/{key}/content'.format(name=name,key=key)

# generate response code
response = requests.get(url,allow_redirects=True,
            auth = HTTPBasicAuth('semadmin', 'semadmin'))
print(response)

#import model to file

#model name
name = 'KingsCrownBOA1 [0.0].xml'
open(name , 'wb').write(response.content)


