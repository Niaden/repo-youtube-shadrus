import unittest
from django.test import TestCase


class ArticleViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/articles/all/')
        self.assertEqual(resp.status_code, 200)

# class TestBasic(unittest.TestCase):
#     "Basic tests"

#     def test_basic(self):
#         a = 1
#         self.assertEqual(1, a)

#     def test_basic_2(self):
#         a = 1
#         assert a == 1

#     def test_mine(self):
#     	assert 11%6 == 5

#     def test_basic_3(self):
#         a = 4
#         assert a > 1

# class TestBasic2(unittest.TestCase):
#     "Show setup and teardown"

#     def setUp(self):
#         self.a = 1

#     def tearDown(self):
#         del self.a

#     def test_basic1(self):
#         "Basic with setup"

#         self.assertNotEqual(self.a, 2)

#     def test_basic2(self):
#         "Basic2 with setup"
#         assert self.a != 2

#     def test_fail(self):
#         "This test should fail"
#         assert self.a == 2


# class qSimpleTest(TestCase):
#     def test_qbasic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 3)
