import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
import datetime


random.seed(100)

def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    
class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()

my_bootstrap_servers = "b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098"

topic_dict = {'0a4ac73a0561.pin':'Pinterest Data', 
              '0a4ac73a0561.geo':'Geographic Data',
              '0a4ac73a0561.user':'User Data'}

# def send_to_api(data, topic):

#     invoke_url = f"https://nsfytprkye.execute-api.us-east-1.amazonaws.com/demo/topic/"
#     headers = {'Content-Type':  'application/vnd.kafka.json.v2+json'}

#     if topic == '0a4ac73a0561.pin':
#         corrected_data = data
#     else:
#         corrected_data = {key.replace('ind', 'index'): value for key, value in data.items()}

#     payload = json.dumps({
#         "records":[
#             {"value": corrected_data}
#             ]
#         }, cls=DateTimeEncoder)

#     response = requests.request("POST", invoke_url, headers=headers, data=payload)
#     print(payload)
#     print(response.status_code)
#     print(response.json()) 

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            ### Send pin_result JSON message
            invoke_url = "https://nsfytprkye.execute-api.us-east-1.amazonaws.com/demo/topic/0a4ac73a0561.pin"
            payload = json.dumps({
                "records": [
                    {
                        "value": {"index": pin_result["index"],
                                  "unique_id": pin_result["unique_id"],
                                  "title": pin_result["title"],
                                  "description": pin_result["description"],
                                  "poster_name": pin_result["poster_name"],
                                  "follower_count": pin_result["follower_count"],
                                  "tag_list": pin_result["tag_list"],
                                  "is_image_or_video": pin_result["is_image_or_video"],
                                  "image_src": pin_result["image_src"],
                                  "downloaded": pin_result["downloaded"],
                                  "save_location": pin_result["save_location"],
                                  "category": pin_result["category"]}
                    }
                ]
            })
            headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            response = requests.request("POST", invoke_url, headers=headers, data=payload)

            ### Send geo_result JSON message
            invoke_url = "https://nsfytprkye.execute-api.us-east-1.amazonaws.com/demo/topic/0a4ac73a0561.geo"
            payload = json.dumps({
                "records": [
                    {
                        "value": {"ind": geo_result["ind"],
                                  "timestamp": serialize_datetime(geo_result["timestamp"]),
                                  "latitude": geo_result["latitude"],
                                  "longitude": geo_result["longitude"],
                                  "country": geo_result["country"]}
                    }
                ]
            })
            headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            response = requests.request("POST", invoke_url, headers=headers, data=payload)
            
            ### Send user_result JSON message
            invoke_url = "https://nsfytprkye.execute-api.us-east-1.amazonaws.com/demo/topic/0a4ac73a0561.user"
            payload = json.dumps({
                "records": [
                    {
                        "value": {"ind": user_result["ind"],
                                  "first_name": user_result["first_name"],
                                  "last_name": user_result["last_name"],
                                  "age": user_result["age"],
                                  "date_joined": serialize_datetime(user_result["date_joined"])}
                    }
                ]
            })
            headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            response = requests.request("POST", invoke_url, headers=headers, data=payload)

        print(response.status_code)            


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
