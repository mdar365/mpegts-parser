# MPEGTS Parser - Spalk Tech Test
This is a webservice for parsing .ts files and returns unique PIDs in hex format

To run the application, you need Python v3.9.6. To download the required modules, run the following command (Make sure you are in the project's root directory):

`pip install -r requirements.txt`

Afterwards, you need to run the server-side using:

`python server/app.py`

endpoint for parsing is http://127.0.0.1:5000/parse

To test parsing a file, run the following command:

`python client/parser_client.py <mpegts file path>`

Response should be printed in standard output shortly after

**Note:** A couple of .ts files have been added in the client directory for your convenience. Run the following commands to test those files:

`python client/parser_client.py client/test_failure.ts` Should give an error and exit with code 1

`python client/parser_client.py client/test_success.ts` Should run successfully and exit with code 0


## Modifying host and port
Server host is 127.0.0.1 and port is 5000. If a different host or port are required, they can be altered in 
`server/config.py`

## Tests
To run tests, use the following commands:

`python server/tests/unit_tests.py`

`python server/tests/integration_tests.py` For integration tests, server needs to be started first otherwise the tests will fail
