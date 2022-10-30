from .user import User
from .post import Post
from db.connector import Connector

class Todo():
  def __init__(self, dev=False):
    self.user_conn = Connector('users', dev=dev)
    self.post_conn = Connector('posts', dev=dev)

  """
    User Operations
  """
  def create_new_user(self, firstname):
    user_list = self.user_conn.get_data()
    user = User(firstname)
    user_list.append(user.__dict__)
    self.user_conn.write(user_list)

    return user.owner_id

  def get_user_count(self):
    user_list = self.user_conn.get_data()
    return len(user_list)

  def edit_username(self, owner_id, firstname):
    user_list = self.user_conn.get_data()
    for user in user_list:
      if user['owner_id'] == owner_id:
        user['firstname'] = firstname
        break
    self.user_conn.write(user_list)

  def remove_user(self, owner_id):
    user_list = self.user_conn.get_data()

    res = list(filter(lambda user: user['owner_id'] != owner_id, user_list))

    self.user_conn.write(res)

  """
    Post Operations
  """
  def add_new_post(self, owner_id, content):
    post = Post(owner_id, content)

    post_list = self.post_conn.get_data()
    post_list.append(post.__dict__)
    
    self.post_conn.write(post_list)

    return post.post_id

  def get_all_owner_posts(self, owner_id):
    post_list = self.post_conn.get_data()

    owner_posts = list(filter( lambda post: post['owner_id'] == owner_id, post_list ))

    return owner_posts

  def get_owner_post_count(self, owner_id):
    return len(self.get_all_owner_posts(owner_id))

  def edit_post(self, post_id, content):
    post_list = self.post_conn.get_data()

    for post in post_list:
      if post['post_id'] == post_id:
        post['content'] = content
        break
    self.post_conn.write(post_list)

  def remove_post(self, post_id):
    post_list = self.post_conn.get_data()

    posts = list(filter( lambda post: post['post_id'] != post_id, post_list ))
    self.post_conn.write(posts)