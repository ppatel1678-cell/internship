import allure_behave
from allure_behave.utils import scenario_name
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from applications.applications import Application
from selenium import webdriver

#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/reelly_secondary_deals.feature


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    mobile_emulation = {
        "deviceMetrics": {"width": 500, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    #Headless mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service=Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

    # bs_user = 'poojap_n58Du0'
    # bs_key = 'jFHNdxSxEVo9CJ5NkVsV'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()

    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "11",
    #     'browserName': 'edge',
    #     'sessionName': scenario_name}

    # bstack_options = {
    #     'deviceName': 'iPhone 12 Pro',
    #     'osVersion': '18',
    #     'browserName': 'chrome',
    #     'deviceOrientation': 'portrait',
    #     'sessionName': scenario_name}

    # bstack_options = {
    #          'deviceName': 'iPhone 11 Pro',
    #          'osVersion': '15',
    #         'browserName': 'firefox',
    #         'deviceOrientation': 'portrait',
    #          'sessionName': scenario_name}

    # bstack_options = {'deviceName': 'Samsung Galaxy S24',
    #                   'osVersion': '14.0',
    #                   'browserName': 'edge',
    #                   'deviceOrientation' : 'portrait',
    #                   'sessionName' : scenario_name}

    # bstack_options = {
    #          'deviceName': 'Samsung Galaxy S20 Ultra',
    #          'osVersion': '13.0',
    #          'browserName': 'samsung',
    #          'deviceOrientation': 'portrait',
    #         'sessionName': scenario_name}

    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()

    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)
    # context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
