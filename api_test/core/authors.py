import requests

url = "https://fakerestapi.azurewebsites.net/api"


def get_all_authors():
    endpoint = "/authors"
    petition = requests.get(url + endpoint)
    return petition


def get_author(id):
    endpoint = "/authors/{}".format(str(id))
    petition = requests.get(url + endpoint)
    return petition


def get_authors_books(id_book):
    endpoint = "/authors/books/{}".format(str(id_book))
    petition = requests.get(url + endpoint)
    return petition


def create_author(id, id_book, first_name, last_name):
    endpoint = "/authors"
    headers = {"Content-Type": "application/json"}
    payload = {
        "Author": {
                "ID": id,
                "IDBook": id_book,
                "FirstName ": first_name,
                "LastName ": last_name
               }
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def edit_author(id, id_book, first_name, last_name):
    endpoint = "/authors/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
         "Author": {
                "ID": "0",
                "IDBook": id_book,
                "FirstName ": first_name,
                "LastName ": last_name
               }
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def delete_author(id):
    endpoint = "/authors/{}".format(str(id))
    petition = requests.delete(url + endpoint)
    return petition
