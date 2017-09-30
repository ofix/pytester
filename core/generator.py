import random
import os
import time
from datetime import datetime
from addr import addr  # 地址码

class Generator:
    def __init__(self):
        pass
    def idCard(self):
        IdCardGenerator.run()
    def username(self):
        UserNameGenerator.run()
        pass
    def password(self):
        PasswordGenerator.run()
        pass
class PasswordGenerator:
    def __init__(self,mode):
        self._mode = mode
    @staticmethod
    def run(mode):
        pass
class UserNameGenerator:
    def __init__(self,mode):
        self._mode = mode

'''身份证随机生成'''
class IdCardGenerator:
    def __init__(self):
        pass
    '''获得校验码算法'''
    @staticmethod
    def getCheckBit(id17):
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 十七位数字本体码权重
        validate = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']  # mod11,对应校验码字符值
        sum = 0
        for i in range(0, len(id17)):
            sum = sum + int(id17[i]) * weight[i]
        mod = sum % 11
        return validate[mod]
    @staticmethod
    def run():
        '''产生随机可用身份证号，sex = 1表示男性，sex = 0表示女性'''
        # 地址码产生
        _addr = random.randint(0, len(addr))  # 随机选择一个值
        addr_id = addr[_addr][0]
        addr_name = addr[_addr][1]
        idNumber = str(addr_id)
        # 出生日期码
        start, end = "1960-01-01", "2000-12-30"  # 生日起止日期
        days = (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days + 1
        birthDays = datetime.strftime(
            datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days)), "%Y%m%d")
        idNumber = idNumber + str(birthDays)
        # 顺序码
        for i in range(2):  # 产生前面的随机值
            n = random.randint(0, 9)  # 最后一个值可以包括
            idNumber = idNumber + str(n)
        # 性别数字码
        sexId = random.randrange(sex, 10, step=2)  # 性别码
        idNumber = idNumber + str(sexId)
        # 校验码
        checkOut = IdCardGenerator.getCheckBit(idNumber)
        idNumber = idNumber + str(checkOut)
        return idNumber, addr_name, addr_id, birthDays, sex, checkOut

class UserNameGenerator:
    def __init__(self):
        pass
