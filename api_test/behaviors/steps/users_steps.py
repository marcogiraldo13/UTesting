from behave import *
from api_test.test.test_users import ApiRequestsUsers

test = ApiRequestsUsers()

@when(u'Consulto todos los usuarios')
def step_impl(context):
    test.test_get_all_users()


@then(u'Trae todos los usuarios')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto un usuario con codigo "id"')
def step_impl(context):
    test.test_get_user(1)


@then(u'trae la informacion de ese usuario')
def step_impl(context):
    test.test_validate_status_code(200)
