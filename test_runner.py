import pytest
from test_scripts.test_cases.test_vtiger import HomeVtigerLogin


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_VtigerProj():
    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.hv = HomeVtigerLogin(self.driver)

    def test_tc_001_add_product_and_verify(self):
        self.hv.loginToApp()