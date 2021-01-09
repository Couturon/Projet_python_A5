import requests
import json

url = 'http://127.0.0.1:5000/api/'

data = [[0.14814815, 0.10493191, 0.        , 0.        , 0.02054795,
       0.02490572, 0.        , 0.02222222, 0.22971109, 0.        ,
       0.14285714, 0.08333333, 0.25      , 0.05263158, 1.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 1.        , 0.        , 0.        ,
       0.        , 0.        , 1.        ]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
if (r.text == '"[1]"\n'):
    print(r, r.text)
    print("Le client va effectuer une commande")
else :
    print(r, r.text)
    print("Le client ne va pas effectuer de commande")