import random
import os
import time
from datetime import datetime
from enum import Enum
from core.globals import prefix
from core.globals import username_prefix
from addr import addr  # 地址码

class GenerateMode(Enum):
    Normal = 1
    Rand = 2
class Generator:
    def __init__(self):
        pass
    def idCard(self):
        IdCardGenerator.run()
    def username(self):
        UserNameGenerator.run(GenerateMode.Normal)
        pass
    def password(self):
        PasswordGenerator.run(GenerateMode.Normal)
        pass
class PasswordGenerator:
    def __init__(self):
        pass
    @staticmethod
    def run(mode):
        if mode == GenerateMode.Normal:
            return "123456"
        else:
            seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
            w = []
            for i in range(8):
                w.append(random.choice(seed))
            pwd = ''.join(w)
            return pwd
class UserNameGenerator:
    def __init__(self):
        pass
    @staticmethod
    def run(mode):
        if mode == GenerateMode.Normal:
            return username_prefix+UserNameGenerator.getNextUserId()
        else:
            seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            w = []
            for i in range(8):
                w.append(random.choice(seed))
            user = ''.join(w)
            return user
    @staticmethod
    def getNextUserId():
        pass

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
        id_no = str(addr_id)
        # 出生日期码
        start, end = "1960-01-01", "2000-12-30"  # 生日起止日期
        days = (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days + 1
        birth_day = datetime.strftime(
            datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days)), "%Y%m%d")
        id_no = id_no + str(birth_day)
        # 顺序码
        for i in range(2):  # 产生前面的随机值
            n = random.randint(0, 9)  # 最后一个值可以包括
            id_no = id_no + str(n)
        # 性别数字码
        sexId = random.randrange(sex, 10, step=2)  # 性别码
        id_no = id_no + str(sexId)
        # 校验码
        checkOut = IdCardGenerator.getCheckBit(id_no)
        id_no = id_no + str(checkOut)
        return id_no, addr_name, addr_id, birth_day, sex, checkOut