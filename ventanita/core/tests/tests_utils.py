from django.test import TestCase

from core.utils import get_item_from_list


class TestCoreUtils(TestCase):
    def test_get_item_from_list(self):
        my_list = ['', 'MIGUEL GRAU']
        expected = 'MIGUEL GRAU'
        result = get_item_from_list(my_list, 1)
        self.assertEqual(expected, result)

    def test_get_item_from_list_empty(self):
        my_list = ['', 'MIGUEL GRAU']
        expected = ''
        result = get_item_from_list(my_list, 10)
        self.assertEqual(expected, result)
