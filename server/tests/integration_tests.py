import unittest
import sys
import os

sys.path.insert(1, os.getcwd())
import common_utils

test_files_directory = os.getcwd()

class ServerTest(unittest.TestCase):

    def test_parse_successfully(self):
        try:
            response = common_utils.send_post_request(test_files_directory + "/server/tests/test_files/test_success.ts")
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                '{"uniquePids":["0x0","0x11","0x20","0x21","0x22","0x23","0x24","0x25","0x1fff"]}',
                response.text.replace("\n", "").replace(" ", ""))
        except ConnectionError as e:
            print("Test failed with a connection error, make sure server is running first before starting the test")
            print("ERROR: ", str(e))

    def test_ParsingException(self):
        try:
            response = common_utils.send_post_request(test_files_directory + "/server/tests/test_files/test_failure.ts")
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                '{  "error": "No sync byte present in packet 20535, offset 3860580"}',
                response.text.replace("\n", "").strip())
        except ConnectionError as e:
            print("Test failed with a connection error, make sure server is running first before starting the test")
            print("ERROR: ", str(e))


if __name__ == '__main__':
    unittest.main()
