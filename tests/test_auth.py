import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_locked_out_user(page):
    login = LoginPage(page)
    login.navigate_to()
    login.login("locked_out_user", "secret_sauce")
    login.verify_error_displayed("Epic sadface: Sorry, this user has been locked out.")