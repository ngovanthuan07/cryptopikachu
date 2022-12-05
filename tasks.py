import requests
import time
import mysql.connector
from datetime import datetime
from mysql.connector import Error

connection = mysql.connector.connect(
    host='localhost',
    database='crypto_python',
    user='root',
    password=''
)

def insert_data():
    apiKey = "d6b8e8027f1d8d68f0f86da76b79f6f4d1b9fd5dd63e3c2b452e8c3dea28e3eb"
    limit = '&limit=' + str(5)
    tsym = '&tsym=USD'
    API_KEY = '&api_key=' + str(apiKey)
    url = 'https://min-api.cryptocompare.com/data/top/totaltoptiervolfull' + '?'  + limit + tsym + API_KEY

    response = requests.get(url).json()
    
    for data in response['Data']:    
        crypto_id = data['CoinInfo']['Id']
        name = data['CoinInfo']['Name']
        fullname = data['CoinInfo']['FullName']
        internal = data['CoinInfo']['Internal']
        image_url = data['CoinInfo']['ImageUrl']
        url = data['CoinInfo']['Url']
        price = data['RAW']['USD']['PRICE']
        top_tier_volume_24_hour_to  = data['RAW']['USD']['TOPTIERVOLUME24HOURTO']
        total_volume_24h_to  = data['RAW']['USD']['TOTALVOLUME24HTO']
        total_top_tier_volume_24h_to  = data['RAW']['USD']['TOTALTOPTIERVOLUME24HTO']
        mktcap  = data['RAW']['USD']['MKTCAP']
        change_pct_24_hour  = data['RAW']['USD']['CHANGEPCT24HOUR']


        cursor = connection.cursor()
        cursor.execute("INSERT INTO crypto (crypto_id, name,fullname,internal,image_url, url,price, top_tier_volume_24_hour_to, total_volume_24h_to, total_top_tier_volume_24h_to, mktcap, change_pct_24_hour) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (crypto_id,name,fullname,internal,image_url,url,price,top_tier_volume_24_hour_to,total_volume_24h_to,total_top_tier_volume_24h_to,mktcap,change_pct_24_hour))
        connection.commit()

def update_data():
    apiKey = "d6b8e8027f1d8d68f0f86da76b79f6f4d1b9fd5dd63e3c2b452e8c3dea28e3eb"
    limit = '&limit=' + str(5)
    tsym = '&tsym=USD'
    API_KEY = '&api_key=' + str(apiKey)
    url = 'https://min-api.cryptocompare.com/data/top/totaltoptiervolfull' + '?'  + limit + tsym + API_KEY

    response = requests.get(url).json()

    ids = getAllIds()

    step = 0
    
    for data in response['Data']:    
        crypto_id = data['CoinInfo']['Id']
        name = data['CoinInfo']['Name']
        fullname = data['CoinInfo']['FullName']
        internal = data['CoinInfo']['Internal']
        image_url = data['CoinInfo']['ImageUrl']
        url = data['CoinInfo']['Url']
        price = data['RAW']['USD']['PRICE']
        top_tier_volume_24_hour_to  = data['RAW']['USD']['TOPTIERVOLUME24HOURTO']
        total_volume_24h_to  = data['RAW']['USD']['TOTALVOLUME24HTO']
        total_top_tier_volume_24h_to  = data['RAW']['USD']['TOTALTOPTIERVOLUME24HTO']
        mktcap  = data['RAW']['USD']['MKTCAP']
        change_pct_24_hour  = data['RAW']['USD']['CHANGEPCT24HOUR']

        cursor = connection.cursor()

        cursor.execute("""UPDATE crypto SET 
                                            crypto_id = %s, 
                                            name = %s,
                                            fullname = %s,
                                            internal = %s,
                                            image_url = %s, 
                                            url = %s,
                                            price = %s, 
                                            top_tier_volume_24_hour_to = %s, 
                                            total_volume_24h_to = %s, 
                                            total_top_tier_volume_24h_to = %s, 
                                            mktcap = %s, 
                                            change_pct_24_hour = %s 
                                            WHERE id = %s """,
                        (crypto_id,name,fullname,internal,image_url,url,price,top_tier_volume_24_hour_to,total_volume_24h_to,total_top_tier_volume_24h_to,mktcap,change_pct_24_hour,ids[step]))
        step += 1
        connection.commit()

def check_table():
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(id) FROM crypto")
    myresult = cursor.fetchall()
    if(myresult[-1][-1] > 0):
        return True
    return False
        
def getAllIds():
    ids = []
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM crypto")   
    for x in cursor:
        ids.append(x[0])
    return ids

def sleepUpdateCoins():   
    while True:
        if check_table() == False:
            insert_data()
        else:
            update_data()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        time.sleep(5*60)
    



