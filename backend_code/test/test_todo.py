import unittest
import json
from src.todo import Todo

class TestPost(unittest.TestCase):
  def setUp(self):
    self._remove_data_in_documents()

  def test_creates_users(self):
    app = Todo(dev=True)
    expected_firstname = 'mo'
    owner_id = app.create_new_user(expected_firstname)

    self.assertEqual(app.get_user_count(), 1)
    self.assertEqual(app.user_conn.get_data()[0]['owner_id'], owner_id)
    self.assertEqual(app.user_conn.get_data()[0]['firstname'], expected_firstname)
  
  def test_create_new_user_with_profile(self):
    app = Todo(dev=True)
    expected_firstname = 'mo'
    expected_profile_image = 'www.images.png'
    owner_id = app.create_new_user(expected_firstname, expected_profile_image)

  
  def test_edit_user_firstname(self):
    app = Todo(dev=True)
    expected_firstname = 'mo'
    owner_id = app.create_new_user(expected_firstname)

    self.assertEqual(app.get_user_count(), 1)
    self.assertEqual(app.user_conn.get_data()[0]['owner_id'], owner_id)
    self.assertEqual(app.user_conn.get_data()[0]['firstname'], expected_firstname)

    new_firstname = 'meme'
    app.edit_username(owner_id, new_firstname)
    self.assertEqual(app.user_conn.get_data()[0]['firstname'], new_firstname)

  def test_sync_name_change_occurs_inbetween_todo_initialisations(self):
    app = Todo(dev=True)
    expected_firstname = 'mo'
    owner_id = app.create_new_user(expected_firstname)

    self.assertEqual(app.get_user_count(), 1)
    self.assertEqual(app.user_conn.get_data()[0]['owner_id'], owner_id)
    self.assertEqual(app.user_conn.get_data()[0]['firstname'], expected_firstname)

    # Delete the todo and recreate new one
    app = None
    app = Todo(dev=True)
    new_firstname = 'meme'
    app.edit_username(owner_id, new_firstname)
    self.assertEqual(app.user_conn.get_data()[0]['firstname'], new_firstname)
  
  def test_remove_user(self):
    app = Todo(dev=True)
    owner_id = app.create_new_user('cool-guy')
    app.remove_user(owner_id)
    self.assertEqual(app.get_user_count(), 0)
  

  def test_create_new_post(self):
    app = Todo(dev=True)
    owner_id = app.create_new_user('cool-guy')

    expected_message = 'Hello World!'
    post_id = app.add_new_post(owner_id, expected_message)

    self.assertEqual(app.get_owner_post_count(owner_id), 1)
    self.assertEqual(app.get_all_owner_posts(owner_id)[0]['content'], expected_message)
    self.assertEqual(app.get_all_owner_posts(owner_id)[0]['post_id'], post_id)
  
  def test_editing_post(self):
    app = Todo(dev=True)
    owner_id = app.create_new_user('cool-guy')

    expected_message = 'Hello World!'
    post_id = app.add_new_post(owner_id, expected_message)

    changed_post = 'lmao changed code'
    app.edit_post(post_id, changed_post)
    self.assertEqual(app.get_owner_post_count(owner_id), 1)
    self.assertEqual(app.get_all_owner_posts(owner_id)[0]['content'], changed_post)

  def test_remove_post(self):
    app = Todo(dev=True)
    owner_id = app.create_new_user('cool-guy')

    expected_message = 'Hello World!'
    post_id = app.add_new_post(owner_id, expected_message)

    self.assertEqual(app.get_owner_post_count(owner_id), 1)

    app.remove_post(post_id)
    self.assertEqual(app.get_owner_post_count(owner_id), 0)

  
  def _remove_data_in_documents(self):
    for document_type in ['dev-users', 'dev-posts']:
      with open(f'db/{document_type}.json', 'w') as f:
        json.dump([], f)
      f.close()