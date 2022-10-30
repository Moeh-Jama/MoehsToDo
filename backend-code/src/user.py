import uuid

class User():
  def __init__(self, firstname):
    self.firstname = firstname
    self.owner_id = uuid.uuid4().hex
  
  def edit(self, firstname):
    self.firstname = firstname