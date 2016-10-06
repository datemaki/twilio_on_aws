'''
Created on 2016/09/27

@author: datemaki
'''

from __future__ import print_function
#from twilio.rest import TwilioRestClient

#import boto3
#import json

print('Loading function')

def get_device_id_by_phone_number(phone_number):
    #
    # TODO: regularize phone_number
    #


    # match and get the correct deviceId
    if (phone_number == "+8150-3187-6833"):
        deviceId = "DeviceId_0001"

    else:
        deviceId = None


    return deviceId

def lambda_handler(event, context):
    ''' Returns a TwiML to enable a real phone to call a Twilio device.
    This function will be received the following parameters.

    {
        "callIncomingPhoneNumber": "+8150-3187-6833"
    }
    '''
    call_incoming_phone_number = event.get("callIncomingPhoneNumber")
    device_id = get_device_id_by_phone_number(call_incoming_phone_number)

    if (device_id is None):
        res = '<?xml version="1.0" encoding="UTF-8"?><Response><Say language="en-US" loop="0">An error occurred. Your phone number {CallIncomingPhoneNumber} is invalid.</Say></Response>'
    else:
        res = '<?xml version="1.0\" encoding="UTF-8"?><Response><Dial timeout="60"><Client>{ClientName}</Client></Dial></Response>'


    strfmt = {"ClientName": device_id, "CallIncomingPhoneNumber": call_incoming_phone_number}

    return res.format(**strfmt)