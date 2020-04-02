import requests

url = "https://fakerestapi.azurewebsites.net/api"


def get_all_coverphoto():
    endpoint = "/CoverPhotos"
    petition = requests.get(url + endpoint)
    return petition


def get_coverphoto(id):
    endpoint = "/CoverPhotos/{}".format(str(id))
    petition = requests.get(url + endpoint)
    return petition


def get_coverbookphoto(id):
    endpoint = "/CoverPhotos/{}".format(str(id))
    petition = requests.get(url + endpoint)
    return petition


def create_coverphoto(id, id_book, url_dat):
    endpoint = "CoverPhotos"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "IDBook": id_book,
        "Url": url_dat
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def edit_coverphoto(id, id_book, url_dat):
    endpoint = "/CoverPhotos/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": "0",
        "IDBook": id_book,
        "Url": url_dat
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def delete_coverphoto(id):
    endpoint = "/CoverPhotos/{}".format(str(id))
    petition = requests.delete(url + endpoint)
    return petition
