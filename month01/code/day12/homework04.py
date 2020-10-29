"""
    小明使用手机打电话
    要求:增加座机,卫星电话时不影响小明
"""


class User():
    def __init__(self, name):
        self.name = name

    def use_phone(self, phone):
        phone.dialing(self)


class Phone():
    def dialing(self, user):
        pass


class MobilePhone(Phone):
    def dialing(self, user):
        print("%s使用手机打电话" % user.name)


class Telephone(Phone):
    def dialing(self, user):
        print("%s使用座机打电话" % user.name)


class SatelliteTelephone(Phone):
    def dialing(self, user):
        print("%s使用卫星电话打电话" % user.name)


mobilephone01 = MobilePhone()
telephone01 = Telephone()
satellite_telephone01 = SatelliteTelephone()
xm = User('小明')
xm.use_phone(mobilephone01)
xm.use_phone(telephone01)
xm.use_phone(satellite_telephone01)
