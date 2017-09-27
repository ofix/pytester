from core.page import Page
class SettleIn(Page):
    def __init__(self,context,browser):
        url = context.url
        browser = ''
        url = []
        data = []
        ele = []
        Page.__init__(self,context,browser,url,data,ele)
        self.__name = 'settle-in'
        self.__name_cn = '企业入驻页面'
        self.__data = data
        self.__ele = ele
    def action

