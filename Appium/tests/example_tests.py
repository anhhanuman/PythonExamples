from Appium.appium_test import AppiumTest


class ExampleTests(AppiumTest):
    def test_login_error(self):
        self.wait_until('Login', )
