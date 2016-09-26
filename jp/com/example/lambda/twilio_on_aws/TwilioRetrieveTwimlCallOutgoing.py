'''
Created on 2016/09/27

@author: datemaki
'''

from __future__ import print_function
from twilio.rest import TwilioRestClient

import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    return '{"result": "ok"}'