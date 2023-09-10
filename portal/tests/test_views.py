from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.core import mail


class EmailTest(TestCase):
    def test_send_email(self):
        EmailMessage(
            subject="test mail",
            body="This is test mail.",
            from_email="appcorgi@gmail.com",
            to=["xianzaikaishiba@gmail.com", "appcorgi@gmail.com"],
        ).send()

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, "test mail")
        self.assertEqual(mail.outbox[0].body, "This is test mail.")
        self.assertEqual(mail.outbox[0].from_email, "appcorgi@gmail.com")
        self.assertEqual(mail.outbox[0].to, ["xianzaikaishiba@gmail.com", "appcorgi@gmail.com"])
