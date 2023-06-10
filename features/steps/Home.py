from behave import given,when, then

@given(u'whatever')
@when(u'whatever')
@then(u'whatever')
def step_impl(context):
    assert 1 is 1
