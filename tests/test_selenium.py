import os
os.environ['ENV'] = "test"
import unittest

from OnlySnarf.util.config import config
from OnlySnarf.util import defaults as DEFAULT
from OnlySnarf.lib.driver import Driver
from OnlySnarf.util.settings import Settings
from OnlySnarf.snarf import Snarf
# from OnlySnarf.classes.user import User

class TestSelenium(unittest.TestCase):

    def setUp(self):
        config["keep"] = False
        Settings.set_debug("tests")

    def tearDown(self):
        self.driver.exit_all()

    ## Auto ##

    @unittest.skip("todo")
    def test_auto(self):
        config["browser"] = "auto"
        self.driver.init()
        assert self.driver.browser, "unable to launch via auto"

    ## Standard ##

    @unittest.skip("todo")
    def test_chrome(self):
        config["browser"] = "chrome"
        self.driver.init()
        assert self.driver.browser, "unable to launch chrome"

    @unittest.skip("todo")
    def test_firefox(self):
        config["browser"] = "firefox"
        self.driver.init()
        assert self.driver.browser, "unable to launch firefox"

    ## Reconnect ##
    
    @unittest.skip("todo")
    def test_reconnect(self):
        config["browser"] = "reconnect"
        self.driver.init()
        assert self.driver.browser, "unable to launch via reconnect"

    @unittest.skip("todo")
    def test_reconnect_chrome(self):
        config["browser"] = "reconnect-chrome"
        self.driver.init()
        assert self.driver.browser, "unable to launch via reconnect chrome"

    @unittest.skip("todo")
    def test_reconnect_firefox(self):
        config["browser"] = "reconnect-firefox"
        self.driver.init()
        assert self.driver.browser, "unable to launch via reconnect firefox"

    ## Remote ##

    @unittest.skip("todo")
    def test_remote(self):
        config["browser"] = "remote"
        self.driver.init()
        assert self.driver.browser, "unable to launch via remote"
    
    @unittest.skip("todo")
    def test_remote_chrome(self):
        config["browser"] = "remote-chrome"
        self.driver.init()
        assert self.driver.browser, "unable to launch via remote chrome"

    @unittest.skip("todo")
    def test_remote_firefox(self):
        config["browser"] = "remote-firefox"
        self.driver.init()
        assert self.driver.browser, "unable to launch via remote firefox"

############################################################################################

if __name__ == '__main__':
    unittest.main()