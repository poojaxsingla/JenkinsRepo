from playwright.sync_api import Page
from TestScript.Script1 import CommonHelper


def test_verify_UI_LoginPage(browser_fixture):
    browser, context, page = browser_fixture
    CommonHelper.launchWeb(page=page)
    CommonHelper.auth0_signin_Validation(page=page)
