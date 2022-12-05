import requests
from mysql.connector import Error

def getAPIHistory(fsym):
    name = fsym
    apiKey = "d6b8e8027f1d8d68f0f86da76b79f6f4d1b9fd5dd63e3c2b452e8c3dea28e3eb"
    API_KEY = '&api_key=' + str(apiKey)
    tsym = "&tsym=GBP"
    limit = '&limit=' + str(20)
    fsym = '?fsym=' + fsym
    url = "https://min-api.cryptocompare.com/data/v2/histominute" + fsym +tsym + limit + API_KEY
    response = requests.get(url).json()
    return {
        "Name": name,
        "TimeFrom": response['Data']['TimeFrom'],
        "TimeTo": response['Data']['TimeTo'],
        "Data" : response['Data']['Data'],
    }
