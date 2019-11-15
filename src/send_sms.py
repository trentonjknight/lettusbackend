import os
from twilio.rest import Client

def send_sms(msg):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=msg,
                        from_='+16198212180',
                        to='+13053324995'
                    )

    print(message.sid)