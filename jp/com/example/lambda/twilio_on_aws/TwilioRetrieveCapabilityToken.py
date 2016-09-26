'''
Created on 2016/09/25

@author: datemaki
'''

from __future__ import print_function
from twilio.rest import TwilioRestClient

import boto3
import json
from twilio.util import TwilioCapability

print('Loading function')


def get_device_id_by_phone_number (phone_number):
    ''' This function returns a valid deviceId.
    '''

    #
    # TODO: regularize phone_number
    #


    # match and get the correct deviceId
    if (phone_number == "+819011112222"):
        deviceId = "DeviceId_0001"

    else:
        deviceId = None


    return deviceId

def lambda_handler(event, context):
    # configure parameters belong to Twilio
    twilio_account_sid = "{{twilio_accound_sid}}"
    twilio_auth_token = "{{twilio_account_auth_token}}"
    twilio_app_sid = "{{twilio_app_sid}}"

    expiration_time_for_capability_token = 3600



    # get necessary parameter from "event" and "context"
    phone_number = event.phoneNumber


    # Create a Capability token with twilio_account_sid and its twilio_auth_token
    # It enables a Twilio client to receive an incoming call and to make an outgoing call.
    capability = TwilioCapability(twilio_account_sid, twilio_auth_token)
    capability.allow_client_incoming(get_device_id_by_phone_number(phone_number))
    capability.allow_client_outgoing(twilio_app_sid)

    capabilityToken = capability.generate(expiration_time_for_capability_token)

    return capabilityToken

