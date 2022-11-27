import uuid

class User():
  def __init__(self, firstname, profile_image=None):
    self.firstname = firstname
    self.owner_id = uuid.uuid4().hex
    self.profile_image = profile_image
  
  def edit(self, firstname):
    self.firstname = firstname