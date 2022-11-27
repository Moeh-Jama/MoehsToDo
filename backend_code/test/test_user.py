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
  
  def test_owner_with_profile_generated(self):
    expected_firstname = "Jon"
    expected_image_location = "www.images.com/11223.png"
    user = User(expected_firstname, expected_image_location)
    self.assertEqual(user.firstname, expected_firstname)
    self.assertEqual(user.profile_image, expected_image_location)