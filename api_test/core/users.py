import requests

url = "https://fakerestapi.azurewebsites.net/api"


def get_all_users():
    endpoint = "/Users"
    petition = requests.get(url + endpoint)
    return petition


def get_user(id):
    endpoint = "/Users/{}".format(str(id))
    petition = requests.get(url + endpoint)
    return petition


def create_users(id, username, password):
    endpoint = "/Users"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "UserName": username,
        "Password ": password
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def edit_users(id, username, password):
    endpoint = "/Users/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": "0",
        "UserName": username,
        "Password ": password
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def delete_users(id):
    endpoint = "/Users/{}".format(str(id))
    petition = requests.delete(url + endpoint)
    return petition
