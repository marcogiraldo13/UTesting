from behave import *
from api_test.test.test_activities import ApiRequestsActivities

test = ApiRequestsActivities()


@given(u'Estoy en la url del API')
def step_impl(context):
    pass


@when(u'Consulto todas las actividades')
def step_impl(context):
    test.test_get_all_activites()


@then(u'Trae todas las actividades')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una actividad con codigo "id"')
def step_impl(context):
    test.test_get_activity(2)


@then(u'trae la informacion de esa actividad')
def step_impl(context):
    test.test_validate_status_code(200)
