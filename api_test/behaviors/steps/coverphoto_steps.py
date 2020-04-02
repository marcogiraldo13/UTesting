from behave import *
from api_test.test.test_coverphoto import ApiRequestsCoverPhoto

test = ApiRequestsCoverPhoto()

@when(u'Consulto todas las portadas')
def step_impl(context):
    test.test_get_all_coverphoto()


@then(u'Trae todas las portadas')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una portada con codigo "id"')
def step_impl(context):
    test.test_get_coverphoto(1)


@then(u'trae la informacion de esa portada')
def step_impl(context):
    test.test_validate_status_code(200)
