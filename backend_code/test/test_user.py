import unittest
from src.user import User

class TestUser(unittest.TestCase):
  def test_user_created(self):
    user = User("Jon")
    self.assertIsNotNone(user)
  
  def test_firstname_is_assigned(self):
    expected_firstname = "Jon"
    user = User(expected_firstname)
    self.assertEqual(user.firstname, expected_firstname)
  
  def test_owner_id_generated(self):
    user = User("Jon")
    self.assertIsNotNone(user.owner_id)