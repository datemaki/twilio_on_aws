'''
Created on 2016/09/27

@author: datemaki
'''

from __future__ import print_function
import json

print('Loading function')



def lambda_handler(event, context):
    ''' Returns a TwiML to enable a Twilio device to call a real phone.
    This function will be received the following parameters.

    {
        "callerPhoneNumber": "+81-50-3123-4567",
        "callOutgoingPhoneNumber": "+81-90-59876543"
    }
    '''

    print ("event: " + json.dumps(event))
    caller_phone_number = event.get("callerPhoneNumber")
    call_outgoing_phone_number = event.get("callOutgoingPhoneNumber")


    res = '<?xml version="1.0" encoding="UTF-8"?><Response><Dial timeout="60" callerId="{callerId}"><Number>{callOutgoingPhoneNumber}</Number></Dial></Response>'
    strfmt = {"callerId": caller_phone_number, "callOutgoingPhoneNumber": call_outgoing_phone_number}

    print (res.format(**strfmt))

    return res.format(**strfmt)