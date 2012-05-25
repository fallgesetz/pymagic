import pymagic
import unittest
import os

class MagicianTest(unittest.TestCase):
    def test_basic(self):
        mage = pymagic.Magician()

        test_files_path = "%s/../files/" % os.getcwd()
        for file in os.listdir(test_files_path):
            with open(os.path.join(test_files_path, file), "rb") as f:
                result = mage.identify(f)
                print result