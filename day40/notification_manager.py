import smtplib
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

    def send_emails(self, emails, message, google_flight_link):
        my_email = "filipe1@gmail.com"
        password = "senha123"

        subject_msg = "Subject:New Low Price Flight!"
        content_msg = f"{message}\n{google_flight_link}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"{subject_msg}\n\n{content_msg}".
                                        encode('utf-8')
                                    )
