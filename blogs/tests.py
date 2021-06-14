from blogs.models import Post
from django.test import TestCase
import unittest
from django.test import Client


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_list(self):
        # Issue a GET request.
        response = self.client.get('/blogs/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # # Check that the rendered context contains 5 customers.
        print(type(response))
        print(dir(response))
        print(response.context_data.get('object_list'))
        self.assertEqual(len(response.context['page_obj']), 0)

    def test_create(self):
        post = Post.objects.create(title='Hello')
        self.assertEqual(post.title, 'Hellos')