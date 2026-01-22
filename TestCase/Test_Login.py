import allure, os
import pytest
from playwright.sync_api import expect

from Pages.LoginPage.LoginPage import LoginPage
from Utils.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config


class TestLogin:

    @pytest.mark.run(order=1)
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", ReadYaml(os.path.join(Config.test_datas_dir, "TestLoginData.yaml")).read())
    def test_login(self, page, CaseData: dict):
        new_page = LoginPage(page)
        # PrettyAllure(page, CaseData).PrettyAllureCase()
        new_page.goto_login(CaseData["url地址"])
        new_page.fill_username(CaseData["账号"])
        new_page.fill_password(CaseData["密码"])
        new_page.click_login_button()
        expect(new_page.goto_login).to_be_visible()
