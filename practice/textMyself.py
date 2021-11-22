accountSID = 'Nothing_to_see_here'
authToken = 'Blah_blah_blah'
myNumber = 'Are_you_still_here?'
twilioNumber = '|='

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)