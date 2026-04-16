#!/bin/bash

# active virtual
source venv/Scripts/activate

# execute test case
./venv/Scripts/python.exe -m pytest test_app.py

#capture exit code
TEST_RESULT=$?

# return exit code
if [ $TEST_RESULT -eq 0 ]; then
    echo "SUCCESS: All tests passed!"
    exit 0
else
    echo "FAILURE: One or more tests failed."
    exit 1
fi