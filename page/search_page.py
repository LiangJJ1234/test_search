import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SearchPage(BaseAction):

    # 搜索按钮
    search_button = By.XPATH, "content-desc,搜索"
    # 搜索框
    input_text_view = By.ID, "android:id/input"
    # 返回按钮
    back_button = By.XPATH, ["content-desc,返回","index,0"]

    def click_search(self):
        self.click(self.search_button)

    def input_content(self, text):
        self.input_text(self.input_text_view, text)

    def click_back(self):
        self.click(self.back_button)