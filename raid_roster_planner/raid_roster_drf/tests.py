from django.test import TestCase

# Create your tests here.


class BasicTestCase(TestCase):
    def test_nothing(self):
        self.assertEqual(1, 1)
