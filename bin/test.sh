#!/bin/bash
# python3 -m unittest tests/test_snarf.py
# python -m unittest test_snarf.TestSnarf.test_users
# python tests/test_snarf.py -p "users"

pytest tests/selenium
pytest tests/snarf

pytest tests/snarf/test_message.py
pytest tests/snarf/test_users.py


## Authentication ##
python setup.py install && python tests/selenium/test_auth.py

## Selenium Processes ##
python setup.py install && python tests/selenium/test_browsers.py
python setup.py install && python tests/selenium/test_reconnect.py
python setup.py install && python tests/selenium/test_remote.py

## Snarf Processes ##
python setup.py install && python tests/snarf/test_discount.py
python setup.py install && python tests/snarf/test_message.py
python setup.py install && python tests/snarf/test_post.py
python setup.py install && python tests/snarf/test_profile.py
python setup.py install && python tests/snarf/test_promotion.py
python setup.py install && python tests/snarf/test_users.py

## IPFS ##
python setup.py install && python tests/test_ipfs.py

#############################################################################

# Pass:

## Selenium:
# auth
# browsers
# reconnect

## Snarf:
# discount
# message
# post (basic)
# post - schedule, date, time
# post - poll
# users

#############################################################################

# Fail


#############################################################################

# Untested

# ipfs
# profile
# promotion
# remote

# (individual driver / message tests)