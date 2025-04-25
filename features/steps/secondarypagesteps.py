from behave import given,when,then

@when("Click on the “Secondary” option at the left side menu")
def click_secondary(context):
    context.app.sidenavigationpage.click_secondary_button()


@then("Verify the right page opens")
def verify_right_page(context):
    context.app.secondarylistingspage.verify_secondary_url()


@then("Click Filter button")
def click_filter_button(context):
    context.app.secondarylistingspage.click_filters_button()


@then("Wait for side Navigation to pop up")
def wait_for_side_navigation(context):
    context.app.secondarylistingspage.wait_for_side_nav()



@then("Filter products by want to sell")
def want_to_sell(context):
    context.app.secondarylistingspage.want_to_sell_button()



@when("Click Apply Filter button")
def click_apply_filter(context):
    context.app.secondarylistingspage.apply_filter_button()



@then("Verify every product has for sale tag")
def verify_sale_tag(context):
    context.app.secondarylistingspage.verify_for_sale_tag()










