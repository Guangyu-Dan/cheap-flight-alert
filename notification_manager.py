from twilio.rest import Client

TWILIO_SID = 'AC8c573f0e39dc3bf340bcd0c03e023642'
TWILIO_AUTH_TOKEN = '68327d8308bc250926480dfbf81344a5'
TWILIO_VIRTUAL_NUMBER = '+19377499583'
TWILIO_VERIFIED_NUMBER = '+13122738538'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)