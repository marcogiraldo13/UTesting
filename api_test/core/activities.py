import requests

url = "https://fakerestapi.azurewebsites.net/api"


def get_all_activities():
    endpoint = "/activities"
    petition = requests.get(url + endpoint)
    return petition


def get_activity(id):
    endpoint = "/activities/{}".format(str(id))
    petition = requests.get(url + endpoint)
    return petition


def create_activity(id, activity_name, date, status):
    endpoint = "/activities"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(activity_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def edit_activity(id, activity_name, date, status):
    endpoint = "/activities/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": "0",
        "Title": "{}".format(activity_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def delete_activity(id):
    endpoint = "/activities/{}".format(str(id))
    petition = requests.delete(url + endpoint)
    return petition
