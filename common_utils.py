import requests


def read_file_as_bytes(file_path):
    with open(file_path, 'rb') as f:
        byte_data = f.read()
    return bytearray(byte_data)


def send_post_request(filepath):
    file_contents = read_file_as_bytes(filepath)
    return requests.post(url='http://127.0.0.1:5000/parse', data=file_contents)
