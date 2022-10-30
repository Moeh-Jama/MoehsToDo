import uuid

class Post():
  def __init__(self, owner_id, content):
    self.post_id = uuid.uuid4()
    self.owner_id = owner_id
    self.content = content
    
  def save(self):
    pass

  def edit(self, content):
    pass