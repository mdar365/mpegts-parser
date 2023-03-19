import os
import random
import secrets
import sys
import unittest

sys.path.insert(1, os.getcwd())

import server.parser as parser


class ParsingTest(unittest.TestCase):

    def test_parseSuccessfully(self):
        # Convert the bytes to hex format
        byte_list = [0x47, 0x0, 0x01]
        hex_values = [int(hex(random.randint(0, 255)), 16) for _ in range(185)]
        byte_array = bytes(byte_list + hex_values)
        output = parser.parse_data(byte_array)
        self.assertEqual(1, len(output))
        self.assertEqual('0x1', output[0])

    # Test parse failing when there is no sync byte
    def test_noSyncByte(self):
        # Convert the bytes to hex format
        byte_list = [0x46, 0x0, 0x01]
        hex_values = [int(hex(random.randint(0, 255)), 16) for _ in range(185)]
        byte_array = bytes(byte_list + hex_values)
        parser.parse_data(byte_array)
        self.assertRaises(parser.ParsingException)

    # Test remove duplicates
    def test_noDuplicates(self):
        # Convert the bytes to hex format
        byte_list = [0x47, 0x0, 0x01]
        random_hex_values = [int(hex(random.randint(0, 255)), 16) for _ in range(185)]
        byte_array = bytes(byte_list + random_hex_values + byte_list + random_hex_values)
        output = parser.parse_data(byte_array)
        self.assertEqual(1, len(output))
        self.assertEqual('0x1', output[0])

    # Test remove duplicates
    def test_sortListOfPids(self):
        # Convert the bytes to hex format
        first_byte_list = [0x47, 0x35, 0x42]  # 0x1542
        random_hex_values = [int(hex(random.randint(0, 255)), 16) for _ in range(185)]
        second_byte_list = [0x47, 0x0, 0x01]  # 0x1

        byte_array = bytes(first_byte_list + random_hex_values + second_byte_list + random_hex_values)
        output = parser.parse_data(byte_array)
        self.assertEqual(2, len(output))
        self.assertEqual('0x1', output[0])
        self.assertEqual('0x1542', output[1])

if __name__ == '__main__':
    unittest.main()