accountSID = 'AC6b214198cce1c839e59f0e036a364fbb'
authToken = '8cdbb0c1a9fcd2639cb00831f53280cb'
myNumber = '+19789305996'
twilioNumber = '+18329475832'

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)