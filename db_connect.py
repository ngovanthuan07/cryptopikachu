import mysql.connector
from mysql.connector import Error
from connection import connect_db

def query():
    list = []
    connection = connect_db()
    try:
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("""SELECT crypto_id, name,fullname,internal,image_url, url,price, top_tier_volume_24_hour_to, total_volume_24h_to, total_top_tier_volume_24h_to, mktcap, change_pct_24_hour 
                              FROM crypto""")
            for x in cursor:
                list.append({
                    "crypto_id": x[0],
                    "name": x[1],
                    "fullname": x[2],
                    "internal": x[3],
                    "image_url": x[4],
                    "url": x[5],
                    "price": x[6],
                    "top_tier_volume_24_hour_to": x[7],
                    "total_volume_24h_to": x[8],
                    "total_top_tier_volume_24h_to": x[9],
                    "mktcap": x[10],
                    "change_pct_24_hour": x[11],
                })
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return list


def queryName():
    list = []
    connection = connect_db()
    try:
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM crypto")
            for x in cursor:
                list.append(x[0])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return list
