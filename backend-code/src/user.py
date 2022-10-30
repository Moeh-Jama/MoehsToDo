import uuid

class User():
  def __init__(self, firstname):
    self.firstname = firstname
    self.owner_id = uuid.uuid4()
  
  def edit(self, firstname):
    pass

  def save(self):
    pass