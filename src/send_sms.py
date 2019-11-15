from twilio.rest import Client

def send_msg(number, msg):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACe16721e90a217d2a95553c71905c6257'
    auth_token = '5b0806499ca4d8428dfd360442b1e974'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Lettus Notification: Water your crop and turn on the lights!",
                        from_='+16198212180',
                        to='+13053324995'
                    )

    print(message.sid)