import json

class Connector():
  def __init__(self, document_type, dev=False):
      self.document_type = document_type
      if dev:
        self.document_type = f"dev-{self.document_type}"
      self.data = []
      self.load()
  
  def load(self):
    with open(f'db/{self.document_type}.json', 'r') as f:
      self.data = json.load(f)
    f.close()
  
  def write(self, data):
    self.data = data
    with open(f'db/{self.document_type}.json', 'w') as f:
      json.dump(self.data, f)
  
  """
    Misc calls to get data and update it.
  """
  def get_data(self):
    return self.data
  
  def update_data(self, data):
    self.data
