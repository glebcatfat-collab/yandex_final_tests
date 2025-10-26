import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,json=body,headers=data.headers)

def get_new_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_KIT_PATH + str(track))
