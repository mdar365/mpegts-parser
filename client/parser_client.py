#!/usr/bin/env python
import os.path
import sys
import requests

sys.path.insert(1, os.getcwd())

import common_utils


def main():
    response = common_utils.send_post_request(sys.argv[1])
    print(response.content.decode("utf-8"))
    if "error" in str(response.content):
        exit(1)
    exit(0)


if __name__ == "__main__":
    main()
