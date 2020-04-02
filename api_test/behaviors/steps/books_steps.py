from behave import *
from api_test.test.test_books import ApiRequestsBooks

test = ApiRequestsBooks()

@when(u'Consulto todos los libros')
def step_impl(context):
    test.test_get_all_books()


@then(u'Trae todos los libros')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto un libro con codigo "id"')
def step_impl(context):
    test.test_get_book(1)


@then(u'trae la informacion de ese libro')
def step_impl(context):
    test.test_validate_status_code(200)
