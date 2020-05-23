import os,sys
from time import sleep

sys.path.append(os.getcwd())
import pytest
from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import *

def data_with_key(key):
    return yml_data_with_file("search_data")[key]

class TestSearch():

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("text", data_with_key("test_search"))
    def test_search(self, text):
        # 点击放大镜
        self.search_page.click_search()
        # 输入文字
        self.search_page.input_content(text)
        # 点击返回
        self.search_page.click_back()

    @pytest.mark.parametrize("text", data_with_key("test_search1"))
    def test_search1(self, text):
        # 点击放大镜
        self.search_page.click_search()
        # 输入文字
        self.search_page.input_content(text)
        # 点击返回
        self.search_page.click_back()
        sleep(3)