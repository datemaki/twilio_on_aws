'''
Created on 2016/09/25

@author: datemaki
'''

from __future__ import print_function
#from twilio.rest import TwilioRestClient
#import boto3
#import json
from twilio.util import TwilioCapability

print('Loading function')


class UnregisteredPhoneNumberException(Exception):
    def __init__(self,value):
        self.value = value


def get_device_id_by_phone_number (phone_number):
    ''' This function returns a valid deviceId.
        If the parameter "phone_number" is not registered, this function raise an "UnregisteredPhoneNumberException".
    '''

    # regularize the input string "phone_number" to match registered phone numbers.
    phone_number_wo_hyphen = phone_number.replace('-','')

    # match and get the correct deviceId
    if (phone_number_wo_hyphen == "+815012349876"):
        deviceId = "DeviceId_0001"

    else:
        raise UnregisteredPhoneNumberException('Unregistered phone number "' + phone_number + '"')

    return deviceId


def lambda_handler(event, context):
    ''' Creates and responds a Twilio Capability Token.
    This function will be received a json formatted string like below.
    {"twilioPhoneNumber": "+81-50-1234-9876"}

    This function will return a json formatted string like below.
    If this function succeed, the parameter "success" will be set as True.
    {"capabilityToken": capabilityToken, "success": True}
    '''

    # configure parameters belong to Twilio
    twilio_account_sid = "{{twilio_accound_sid}}"
    twilio_auth_token = "{{twilio_account_auth_token}}"
    twilio_app_sid = "{{twilio_app_sid}}"
    expiration_time_for_capability_token = 3600


    # get necessary parameter from "event" and "context"
    twilio_phone_number = event.get("twilioPhoneNumber")


    # Create a Capability token with twilio_account_sid and its twilio_auth_token
    # It enables a Twilio client to receive an incoming call and to make an outgoing call.
    try:
        capability = TwilioCapability(twilio_account_sid, twilio_auth_token)
        capability.allow_client_incoming(get_device_id_by_phone_number(twilio_phone_number))
        capability.allow_client_outgoing(twilio_app_sid)
        capabilityToken = capability.generate(expiration_time_for_capability_token)
        res = {"capabilityToken": capabilityToken, "success": True}

    except UnregisteredPhoneNumberException:
        res = {"capabilityToken": None, "success": False}

    return res
