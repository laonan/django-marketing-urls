from django.test import TestCase, Client
from urltoken.encoder import UrlTokenEncoder
from .models import MarketingUrl, VisitorLog


class MarketingUrlsTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_url(self):
        m = MarketingUrl.objects.create(original_url='https://www.google.com')
        print('********************************************\n')
        marketing_url = m.marketing_url
        print(f'Marketing Url: {marketing_url}')
        encoder = UrlTokenEncoder('secretkey')
        token =  encoder.encode('example@domain.com')
        click_url = marketing_url + '?t=' + token
        print(f'Click Url: {click_url}')

        c = Client()
        response = c.get(click_url)
        print(f'Response: {response}')

        logs = VisitorLog.objects.all()
        for log in logs:
            print(f'Log: {log.url} - {log.url_decoded_token} - {log.ip} - {log.create_time}')

        self.assertTrue(True)
