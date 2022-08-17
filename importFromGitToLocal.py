import requests as req

#raw file url
url = 'https://raw.githubusercontent.com/fakemail1865/new_rep/main/folder1/KingsCrownBOA1%20%5B0.0%5D.xml'

with req.get(url) as rq:
    with open('my_xml3.xml','wb') as file:
        file.write(rq.content)