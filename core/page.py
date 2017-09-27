from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.find_element_by_id("kw").send_keys("selenium")
'''
每个页面的测试类
'''
class Page:
    def __init__(self,context,browser,url,data,ele):
        self.__name = 'undefined'
        self.__name_cn = 'undefined'
        self.__url =url
        self.__data = data
        self.__ele  = ele
        self.__context = context
        self.__browser = browser
    # 将参数传递给页面
    def assign(self):
        browser.get(self.__url)
        i = 0
        for data in self.__data:
            self.__browser.find_element_by_id(self.__ele[i]).send_keys(data)
            i = i + 1
    def execute(self):
        if len(self.__data) != len(self.__ele):
            raise Exception('传入参数错误!')
        self.assign()
    def shutdown(self):
        self.__browser.quit()


