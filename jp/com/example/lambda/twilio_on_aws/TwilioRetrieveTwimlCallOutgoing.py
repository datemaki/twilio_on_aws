'''
Created on 2016/09/27

@author: datemaki
'''

from __future__ import print_function
#from twilio.rest import TwilioRestClient

#import boto3
#import json

print('Loading function')



def lambda_handler(event, context):
    ''' Returns a TwiML to enable a Twilio device to call a real phone.
    This function will be received the following parameters.

    {
        "callerPhoneNumber": "+8150-3187-6833",
        "callOutgoingPhoneNumber": "+81-90-5448-4394"
    }
    '''

    print (event)
    caller_phone_number = event.get("callerPhoneNumber")
    call_outgoing_phone_number = event.get("callOutgoingPhoneNumber")


    res = '<?xml version="1.0" encoding="UTF-8"?><Response><Dial timeout="60" callerId="{callerId}"><Number>{callOutgoingPhoneNumber}</Number></Dial></Response>'
    strfmt = {"callerId": caller_phone_number, "callOutgoingPhoneNumber": call_outgoing_phone_number}

    return res.format(**strfmt)