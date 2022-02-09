from twilio.rest import Client
import os


class NotificationManager:
    def __init__(self) -> None:
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.my_phone_number_twilio = os.environ['my_phone_number_twilio']
        self.my_real_phone = os.environ['my_real_phone']

    def send_sms_news(self, body_message):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
                        .create(
                            body=body_message,
                            from_=self.my_phone_number_twilio,
                            to=self.my_real_phone
                        )
        print(message.status)
