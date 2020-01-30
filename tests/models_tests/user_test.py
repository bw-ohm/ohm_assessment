from tests import OhmTestCase


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []

    def test_is_below_tier(self):
        self.chuck.set_tier("Carbon")
        assert self.chuck.is_below_tier("Platinum") == True
        assert self.chuck.is_below_tier("Carbon") == False
        self.chuck.set_tier("Silver")
        assert self.chuck.is_below_tier("Platinum") == True
        assert self.chuck.is_below_tier("Silver") == False
        assert self.chuck.is_below_tier("Carbon") == False
        self.chuck.set_tier("Platinum")
        assert self.chuck.is_below_tier("Platinum") == False
        assert self.chuck.is_below_tier("Silver") == False

