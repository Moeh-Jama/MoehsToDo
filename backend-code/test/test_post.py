import unittest
from src.post import Post

class TestPost(unittest.TestCase):
  def test_post_created(self):
    post = Post('11', 'this is true')
    self.assertIsNotNone(post)
  
  def test_post_created_accurately(self):
    expected_owner_id = '1'
    expected_message = 'welcome to world ;)'
    post = Post(expected_owner_id, expected_message)
    self.assertEqual(post.content, expected_message)
    self.assertEqual(post.owner_id, expected_owner_id)