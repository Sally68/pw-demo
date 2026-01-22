# -*- coding:utf-8 -*-
"""
describe：登录页面
"""
import allure
from BasePage.BasePage import BasePage


class LoginPage(BasePage):
    # 元素定位器
    __username = "//input[@class='el-input__inner' and @type='text']"
    __password = "//input[@class='el-input__inner' and @type='password']"
    # __login_button = '//*[@id=\"app\"]/div/div[2]/div[2]/form/div[4]/div/button/span'
    # page.get_by_text('登录', exact=True)

    def del_auth(self):
        self._del_auth()

    @allure.step("打开登录页面")
    def goto_login(self, url):
        self._goto_url(url)

    @allure.step("输入账号")
    def fill_username(self, value):
        self._fill(self.__username, value)

    @allure.step("输入密码")
    def fill_password(self, value):
        self._fill(self.__password, value)


    @allure.step("点击登录按钮")
    def click_login_button(self):
        self._click(self.page.get_by_role('button', name = "登录"))


    def browser_operation(self, reload=True, forward=False, back=False):
        self._browser_operation(reload=reload, forward=forward, back=back)
