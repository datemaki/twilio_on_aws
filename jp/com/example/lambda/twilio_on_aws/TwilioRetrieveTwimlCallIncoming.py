'''
Created on 2016/09/27

@author: datemaki
'''

from __future__ import print_function
#from twilio.rest import TwilioRestClient

#import boto3
import json

print('Loading function')

def get_client_name_by_phone_number(phone_number):
    # regularize the input string "phone_number" to match registered phone numbers.
    phone_number_wo_hyphen = phone_number.replace('-','')

    # match and get the correct clientName
    if (phone_number_wo_hyphen == "+815031234567"):
        clientName = "DeviceId_0001"

    else:
        clientName = None


    return clientName

def lambda_handler(event, context):
    ''' Returns a TwiML to enable a real phone to call a Twilio device.
    This function will be received the following parameters.

    {
        "Caller": "+819012345678"
        "To": "+815098765432"
    }
    '''

    print ("event: " + json.dumps(event))

    call_incoming_phone_number = event.get("To")
    client_name = get_client_name_by_phone_number(call_incoming_phone_number)

    if (client_name is None):
        res = '<?xml version="1.0" encoding="UTF-8"?><Response><Say language="en-US" loop="0">An error occurred. Your Twilio phone number {CallIncomingPhoneNumber} is invalid.</Say></Response>'
    else:
        res = '<?xml version="1.0\" encoding="UTF-8"?><Response><Dial timeout="60"><Client>{ClientName}</Client></Dial></Response>'


    strfmt = {"ClientName": client_name, "CallIncomingPhoneNumber": call_incoming_phone_number}

    print (res.format(**strfmt))

    return res.format(**strfmt)