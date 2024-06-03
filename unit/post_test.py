from unittest import TestCase
from main import Post


class PostTest(TestCase):
    def test_create_post(self):
        data = Post("Test", "Test code")

        self.assertEqual(data.title, "Test")
        self.assertEqual(data.content, "Test code")
