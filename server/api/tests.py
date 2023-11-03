import json

from django.core.cache import cache
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from api.functions import sum_of_squares, square_of_sums


class SumOfSquaresTestCase(TestCase):
    def test_ten(self):
        assert sum_of_squares(10) == 385

    def test_fifty(self):
        assert sum_of_squares(50) == 42925


class SquareOfSumTestCase(TestCase):
    def test_ten(self):
        assert square_of_sums(10) == 3025

    def test_fifty(self):
        assert square_of_sums(50) == 1625625


class DifferenceTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("difference")

    def test_difference(self):
        assert cache.get('differences_10') is None

        url = self.url + "?number=10"

        response = self.client.get(url)
        assert response.status_code == 200

        content = json.loads(response.content)
        assert set(content.keys()) == {'datetime', 'difference', 'last_datetime', 'number', 'occurrences'}
        assert content["difference"] == 2640

        cached_value = cache.get('differences_10')
        assert cached_value['difference'] == 2640
        assert cached_value['occurrences'] == 1

    def test_bad_value(self):
        url = self.url + "?number=x"
        response = self.client.get(url)
        assert response.status_code == 400


class PythagoreanTripletTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("pythagorean_triplet")

    def test_is_pythagorean_triplet(self):
        assert cache.get('pythagorean_3_4_5') is None

        url = self.url + "?a=3&b=4&c=5"
        response = self.client.get(url)
        assert response.status_code == 200

        content = json.loads(response.content)
        assert set(content.keys()) == {'datetime', 'is_triplet', 'last_datetime', 'product', 'occurrences'}
        assert content["is_triplet"] is True
        assert content["product"] == 60

        cached_value = cache.get('pythagorean_3_4_5')
        assert cached_value['is_triplet'] is True
        assert cached_value['product'] == 60
        assert cached_value['occurrences'] == 1

    def test_is_not_pythagorean_triplet(self):
        assert cache.get('pythagorean_1_2_3') is None

        url = self.url + "?a=1&b=2&c=3"
        response = self.client.get(url)
        assert response.status_code == 200

        content = json.loads(response.content)
        assert set(content.keys()) == {'datetime', 'is_triplet', 'last_datetime', 'product', 'occurrences'}
        assert content["is_triplet"] is False
        assert content["product"] == 6

        cached_value = cache.get('pythagorean_1_2_3')
        assert cached_value['is_triplet'] is False
        assert cached_value['product'] == 6
        assert cached_value['occurrences'] == 1

    def test_bad_value(self):
        url = self.url + "?a=3&b=4&c=five"
        response = self.client.get(url)
        assert response.status_code == 400

    def test_missing_params(self):
        url = self.url + "?a=3&b=4"
        response = self.client.get(url)
        assert response.status_code == 400
