from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from asset.models import Asset


class AssetTest(TestCase):
    fixtures = ['user.json']

    def setUp(self) -> None:
        super().setUp()
        self.client = Client()

    def test_create(self):
        self.client.force_login(User.objects.first())
        response = self.client.post(reverse('asset:create'), data={'name': 'teste'}, follow=True)
        self.assertEqual(response.template_name, ['asset/asset_form.html'])
        asset = Asset.objects.filter(name='teste').first()
        self.assertIsInstance(asset, Asset)
