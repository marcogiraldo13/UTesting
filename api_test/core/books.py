import requests

url = "https://fakerestapi.azurewebsites.net/api"


def get_all_books():
    endpoint = "/books"
    petition = requests.get(url + endpoint)
    return petition


def get_book(id):
    endpoint = "/books/{}".format(str(id))
    petition = requests.get(url + endpoint)
    return petition


def create_book(id, title, description, page_count, excerpt, date):
    endpoint = "/books"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": title,
        "Description ": description,
        "PageCount": page_count,
        "Excerpt": excerpt,
        "PublishDate": "".format(date),
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def edit_book(id, title, description, page_count, excerpt, date):
    endpoint = "/books/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": "0",
        "Title": title,
        "Description ": description,
        "PageCount": page_count,
        "Excerpt": excerpt,
        "PublishDate": "".format(date),
    }
    petition = requests.post(url + endpoint, data=payload, headers=headers)
    return petition


def delete_books(id):
    endpoint = "/books/{}".format(str(id))
    petition = requests.delete(url + endpoint)
    return petition
