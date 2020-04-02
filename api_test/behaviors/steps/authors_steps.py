from behave import *
from api_test.test.test_authors import ApiRequestsAuthors

test = ApiRequestsAuthors()

@when(u'Consulto todos los autores')
def step_impl(context):
    test.test_get_all_authors()


@then(u'Trae todos los autores')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto un autor con codigo "id"')
def step_impl(context):
    test.test_get_author(1)


@then(u'trae la informacion de ese autor')
def step_impl(context):
    test.test_validate_status_code(200)
