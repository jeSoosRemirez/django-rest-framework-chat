from django.test import TestCase
from django.utils import timezone
from chat_app.models import Message
from chat_app.serializers import MessageListSerializer
# from django.test import TestCase


class PostTestCase(TestCase):

    def setUp(self):
        Message.objects.create(
            author='test-author',
            author_email='test-author@gmail.com',
            text="We are testing this",
            created_time=timezone.now(),
        )

    def test_message_is_sent(self):
        """Messages are created"""
        message1 = Message.objects.get(author='test-author')
        self.assertEqual(message1.text, "We are testing this")

    def test_valid_form_data(self):
        form = MessageListSerializer(data={
            'author': "Just testing",
            'text': "Repeated tests make the app foul-proof",
        })
        self.assertTrue(form.is_valid())
        message1 = form.save()
        message1.author = 'test-author'
        message1.save()
        self.assertEqual(message1.text, "Repeated tests make the app foul-proof")

    def test_blank_form_data(self):
        form = MessageListSerializer(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'text': ['This field is required.'],
        })
